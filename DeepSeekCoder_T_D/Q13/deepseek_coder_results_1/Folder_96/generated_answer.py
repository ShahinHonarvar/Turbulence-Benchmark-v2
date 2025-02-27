def find_second_largest_num(numbers):
    if len(numbers) < 52 or 15 >= len(numbers):
        return None
    sublist = numbers[15:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]