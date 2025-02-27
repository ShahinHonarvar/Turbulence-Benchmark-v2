def find_second_largest_num(numbers):
    if len(numbers) < 79 or 17 >= len(numbers):
        return None
    sublist = numbers[17:79]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]