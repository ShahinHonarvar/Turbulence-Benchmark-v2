def find_second_smallest_num(numbers):
    if len(numbers) < 99 or 55 > 98:
        return None
    sublist = sorted(numbers[55:99])
    if len(sublist) < 2:
        return None
    return sublist[1]