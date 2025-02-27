def find_second_largest_num(numbers):
    sublist = numbers[20:31]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]