def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:5]
    largest = max(sublist)
    second_largest = None
    for num in numbers[:4] + numbers[5:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest