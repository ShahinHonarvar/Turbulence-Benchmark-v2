def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = numbers[19:93]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None