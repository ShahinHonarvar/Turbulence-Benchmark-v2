def find_second_largest_num(numbers):
    if len(numbers) < 988:
        return None
    sublist = numbers[686:988]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]