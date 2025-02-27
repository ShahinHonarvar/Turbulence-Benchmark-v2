def find_second_smallest_num(numbers):
    if 43 <= len(numbers) <= 86:
        sublist = sorted(numbers[43:87])
        return sublist[1] if len(sublist) > 1 else None
    return None