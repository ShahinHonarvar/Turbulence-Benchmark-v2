def find_second_largest_num(numbers):
    if len(numbers) < 87 or len(numbers[43:87]) < 2:
        return None
    subset = numbers[43:87]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest