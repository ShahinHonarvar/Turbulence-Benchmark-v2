def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    sublist = numbers[75:86]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]