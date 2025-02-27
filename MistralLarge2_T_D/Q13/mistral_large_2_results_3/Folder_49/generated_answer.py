def find_second_largest_num(numbers):
    if not 80 <= len(numbers) <= 200:
        return None
    subset = numbers[80:201]
    if len(subset) < 2:
        return None
    first_max = max(subset)
    subset.remove(first_max)
    second_max = max(subset)
    return second_max