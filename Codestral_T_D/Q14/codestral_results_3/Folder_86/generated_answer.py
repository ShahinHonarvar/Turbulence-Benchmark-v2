def find_second_smallest_num(numbers):
    if 33 <= len(numbers) <= 36:
        subset = sorted(numbers[33:37])
        return subset[1] if len(subset) > 1 else None
    else:
        return None