def find_second_largest_num(numbers):
    if len(numbers) < 51 or 22 >= len(numbers):
        return None
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]