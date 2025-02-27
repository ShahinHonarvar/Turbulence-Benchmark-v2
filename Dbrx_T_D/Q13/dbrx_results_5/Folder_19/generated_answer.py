def find_second_largest_num(numbers):
    if len(numbers) < 5 or len(numbers) > 6:
        return None
    sublist = numbers[3:6]
    if len(sublist) == 4:
        sublist.pop(0)
    if len(sublist) < 2:
        return None
    first_largest = max(sublist[0], sublist[1])
    second_largest = min(sublist[0], sublist[1])
    for num in sublist[2:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == first_largest:
        return None
    else:
        return second_largest