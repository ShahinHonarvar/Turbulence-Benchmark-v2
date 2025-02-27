def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[30:88]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]