def find_second_largest_num(numbers):
    if len(numbers) < 33 or len(numbers[28:33]) <= 1:
        return None
    subset = numbers[28:33]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]