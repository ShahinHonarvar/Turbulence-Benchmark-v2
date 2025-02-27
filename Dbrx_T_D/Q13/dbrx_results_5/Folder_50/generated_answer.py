def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 15:
        return None
    sublist = numbers[70:85]
    if len(sublist) < 2:
        return None
    first, second = (max(sublist[0], sublist[1]), min(sublist[0], sublist[1]))
    for num in sublist[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == first:
        return None
    else:
        return second