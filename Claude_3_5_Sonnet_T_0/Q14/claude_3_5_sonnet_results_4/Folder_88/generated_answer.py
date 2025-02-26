def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[6:9]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None