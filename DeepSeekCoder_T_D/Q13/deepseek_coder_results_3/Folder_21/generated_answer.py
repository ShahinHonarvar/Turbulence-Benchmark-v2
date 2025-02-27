def find_second_largest_num(numbers):
    if len(numbers) < 976 or len(numbers) < 639:
        return None
    sublist = numbers[639:976]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]