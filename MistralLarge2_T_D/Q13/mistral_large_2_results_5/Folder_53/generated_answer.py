def find_second_largest_num(numbers):
    if len(numbers) <= 200:
        return None
    subset = numbers[100:201]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]