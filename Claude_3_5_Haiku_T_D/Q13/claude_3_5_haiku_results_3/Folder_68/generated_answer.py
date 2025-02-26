def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    subset = numbers[:9]
    sorted_unique = sorted(set(subset), reverse=True)
    return sorted_unique[1] if len(sorted_unique) > 1 else None