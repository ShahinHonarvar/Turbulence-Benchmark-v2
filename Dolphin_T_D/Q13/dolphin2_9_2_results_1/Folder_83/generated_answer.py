def find_second_largest_num(numbers):
    if 90 < len(numbers) <= 90:
        return None
    sublist = numbers[90:91]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]