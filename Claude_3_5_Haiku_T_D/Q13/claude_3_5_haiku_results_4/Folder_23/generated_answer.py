def find_second_largest_num(numbers):
    if len(numbers) < 54 or not 52 <= len(numbers) - 1:
        return None
    subset = numbers[52:72]
    subset.sort(reverse=True)
    return subset[1] if len(subset) >= 2 else None