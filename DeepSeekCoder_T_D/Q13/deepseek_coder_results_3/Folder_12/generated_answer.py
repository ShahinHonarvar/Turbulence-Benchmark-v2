def find_second_largest_num(numbers):
    if len(numbers) < 65 or 14 >= len(numbers):
        return None
    sublist = numbers[14:65]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]