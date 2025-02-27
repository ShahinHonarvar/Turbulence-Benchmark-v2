def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    sublist = numbers[33:37]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]