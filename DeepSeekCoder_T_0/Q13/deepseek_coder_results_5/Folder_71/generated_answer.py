def find_second_largest_num(numbers):
    if len(numbers) < 53:
        return None
    sublist = numbers[26:53]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]