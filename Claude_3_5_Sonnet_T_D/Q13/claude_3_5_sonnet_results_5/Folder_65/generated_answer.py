def find_second_largest_num(numbers):
    if len(numbers) < 99:
        return None
    sublist = numbers[56:99]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None