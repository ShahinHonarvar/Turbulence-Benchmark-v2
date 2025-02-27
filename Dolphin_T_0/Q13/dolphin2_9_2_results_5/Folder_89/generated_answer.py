def find_second_largest_num(lst):
    sublist = lst[56:83]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    if len(sublist) == 0:
        return None
    second_largest = max(sublist)
    return second_largest