def find_second_largest_num(numbers):
    if len(numbers) < 51:
        return None
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]