def find_second_smallest_num(numbers):
    if 29 <= len(numbers) <= 93:
        sublist = sorted(numbers[29:94])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None