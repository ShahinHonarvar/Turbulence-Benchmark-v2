def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[:7]) < 2:
        return None
    subset = numbers[:7]
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest