def find_second_largest_num(numbers):
    if len(numbers) <= 200:
        return None
    subset = numbers[80:201]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]