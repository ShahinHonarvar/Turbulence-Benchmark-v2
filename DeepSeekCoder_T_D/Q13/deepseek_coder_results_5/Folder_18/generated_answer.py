def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    sublist = numbers[35:50]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]