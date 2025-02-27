def find_second_largest_num(list_numbers):
    sublist = list_numbers[75:86]
    sublist = list(set(sublist))
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]