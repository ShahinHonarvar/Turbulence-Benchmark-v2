def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    sublist = numbers[75:89]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]