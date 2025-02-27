def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    sublist = numbers[32:36]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]