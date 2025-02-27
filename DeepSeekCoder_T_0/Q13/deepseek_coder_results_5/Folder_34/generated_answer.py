def find_second_largest_num(numbers):
    if len(numbers) < 62 or 16 >= len(numbers):
        return None
    sublist = numbers[16:62]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]