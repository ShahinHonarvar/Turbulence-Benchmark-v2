def find_second_largest_num(numbers):
    if len(numbers) < 32 or len(numbers) <= 87:
        return None
    subset = numbers[30:88]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None