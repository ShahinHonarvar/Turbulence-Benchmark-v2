def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    largest = max(lst[0:7])
    lst.remove(largest)
    if not lst:
        return None
    second_largest = max(lst[0:6])
    return second_largest