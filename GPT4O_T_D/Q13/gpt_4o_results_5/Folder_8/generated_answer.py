def find_second_largest_num(numbers):
    sublist = numbers[23:24]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2] if len(sublist) > 1 else None