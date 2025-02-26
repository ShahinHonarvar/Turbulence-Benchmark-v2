def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 248:
        return None
    sublist = numbers[246:751]
    if not sublist:
        return None
    try:
        sorted_sublist = sorted(set(sublist), reverse=True)
        return sorted_sublist[1] if len(sorted_sublist) >= 2 else None
    except (TypeError, ValueError):
        return None