def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    limited_list = numbers[:8]
    if len(limited_list) < 2:
        return None
    sorted_unique = sorted(set(limited_list))
    return sorted_unique[1] if len(sorted_unique) >= 2 else None