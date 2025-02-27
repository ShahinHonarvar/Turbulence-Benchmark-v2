def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sublist = numbers[50:55]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]