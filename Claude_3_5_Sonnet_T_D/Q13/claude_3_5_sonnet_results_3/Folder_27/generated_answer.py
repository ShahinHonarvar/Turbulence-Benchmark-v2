def find_second_largest_num(numbers):
    if len(numbers) < 94 or len(numbers[66:94]) < 2:
        return None
    subset = numbers[66:94]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest