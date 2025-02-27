def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sublist = numbers[29:94]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]