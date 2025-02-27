def find_second_largest_num(numbers):
    sublist = numbers[70:85]
    sublist = list(set(sublist))
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]