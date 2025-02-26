def find_second_largest_num(numbers):
    if len(numbers) < 30 or len(numbers[29:80]) < 2:
        return None
    subset = numbers[29:80]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]