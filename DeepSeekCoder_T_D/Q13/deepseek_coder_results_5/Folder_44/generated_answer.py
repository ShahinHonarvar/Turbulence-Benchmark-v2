def find_second_largest_num(numbers):
    if len(numbers) < 69 or 13 >= len(numbers):
        return None
    sublist = numbers[13:69]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]