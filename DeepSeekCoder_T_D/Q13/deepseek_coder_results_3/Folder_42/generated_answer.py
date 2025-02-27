def find_second_largest_num(numbers):
    if len(numbers) < 80 or 79 - 29 + 1 < 2:
        return None
    sublist = numbers[29:80]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]