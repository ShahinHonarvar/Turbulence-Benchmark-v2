def find_second_largest_num(numbers):
    if len(numbers) < 23:
        return None
    sublist = numbers[22:89]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None