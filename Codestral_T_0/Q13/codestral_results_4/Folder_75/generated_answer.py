def find_second_largest_num(numbers):
    sublist = numbers[56:58]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]