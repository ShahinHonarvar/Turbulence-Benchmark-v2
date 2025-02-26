def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sublist = numbers[66:94]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest