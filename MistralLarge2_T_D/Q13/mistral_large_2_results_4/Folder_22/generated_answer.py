def find_second_largest_num(numbers):
    if len(numbers) <= 200:
        return None
    subset = numbers[40:201]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    return max(subset)