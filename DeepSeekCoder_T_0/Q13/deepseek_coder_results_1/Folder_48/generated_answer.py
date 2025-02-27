def find_second_largest_num(numbers):
    if len(numbers) < 606:
        return None
    sublist = numbers[533:606]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]