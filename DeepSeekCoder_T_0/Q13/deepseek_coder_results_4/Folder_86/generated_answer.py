def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    sublist = numbers[31:35]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]