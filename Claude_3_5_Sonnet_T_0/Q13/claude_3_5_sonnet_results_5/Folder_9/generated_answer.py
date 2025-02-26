def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers[200:201]) < 2:
        return None
    subset = numbers[200:201]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest