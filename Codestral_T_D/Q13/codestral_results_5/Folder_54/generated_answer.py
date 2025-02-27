def find_second_largest_num(numbers):
    sublist = numbers[34:56]
    sublist.sort()
    if len(sublist) >= 2:
        return sublist[-2]
    else:
        return None