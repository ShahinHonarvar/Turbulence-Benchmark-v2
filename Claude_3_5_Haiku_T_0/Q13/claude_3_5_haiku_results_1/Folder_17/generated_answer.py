def find_second_largest_num(numbers):
    if len(numbers) < 64 or len(numbers) <= 78:
        return None
    subset = numbers[62:79]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None