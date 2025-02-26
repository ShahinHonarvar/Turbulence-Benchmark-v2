def find_second_largest_num(numbers):
    if len(numbers) < 91 or len(numbers[90:91]) < 2:
        return None
    subset = numbers[90:91]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest