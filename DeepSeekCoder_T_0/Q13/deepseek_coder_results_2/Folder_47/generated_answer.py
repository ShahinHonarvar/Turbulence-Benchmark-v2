def find_second_largest_num(numbers):
    if len(numbers) < 77 or 37 >= len(numbers):
        return None
    sublist = numbers[37:77]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]