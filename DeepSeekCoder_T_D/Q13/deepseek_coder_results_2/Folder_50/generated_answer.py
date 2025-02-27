def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    sublist = numbers[70:85]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]