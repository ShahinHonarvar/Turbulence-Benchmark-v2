def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers[1:6]) < 2:
        return None
    subset = numbers[1:6]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest