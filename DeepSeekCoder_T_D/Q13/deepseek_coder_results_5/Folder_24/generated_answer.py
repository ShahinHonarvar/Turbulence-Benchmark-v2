def find_second_largest_num(numbers):
    if len(numbers) < 96:
        return None
    sublist = numbers[74:96]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]