def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    if 975 >= len(numbers) or 639 < 0:
        return None
    sublist = sorted(numbers[639:976])
    if len(sublist) < 2:
        return None
    return sublist[1]