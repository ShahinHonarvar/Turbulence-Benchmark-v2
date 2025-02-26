def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    sublist = numbers[6:7]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest