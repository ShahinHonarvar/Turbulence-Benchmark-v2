def find_second_largest_num(numbers):
    if len(numbers) < 557 or 209 >= len(numbers):
        return None
    sublist = numbers[209:557]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]