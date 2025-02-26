def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 23:
        return None
    sublist = numbers[22:89]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None