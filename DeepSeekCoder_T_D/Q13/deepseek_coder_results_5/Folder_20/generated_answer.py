def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sublist = numbers[56:67]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]