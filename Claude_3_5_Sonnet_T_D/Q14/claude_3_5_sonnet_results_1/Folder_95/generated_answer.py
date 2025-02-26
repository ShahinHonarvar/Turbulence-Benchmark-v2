def find_second_smallest_num(numbers):
    if len(numbers) < 86:
        return None
    sublist = numbers[75:86]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None