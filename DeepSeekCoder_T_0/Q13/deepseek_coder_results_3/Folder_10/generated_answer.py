def find_second_largest_num(numbers):
    if len(numbers) < 60 or 25 >= len(numbers):
        return None
    sublist = numbers[25:60]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]