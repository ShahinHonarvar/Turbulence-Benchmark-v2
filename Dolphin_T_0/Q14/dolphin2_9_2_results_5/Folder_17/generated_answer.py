def find_second_smallest_num(numbers):
    if 28 <= len(numbers) <= 38:
        sublist = sorted(numbers[28:38 + 1])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None