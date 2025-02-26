def find_second_largest_num(numbers):
    if len(numbers) < 58 or not 56 <= len(numbers) <= 83:
        return None
    subset = numbers[56:83]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None