def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    largest = max(lst[0:8])
    lst.remove(largest)
    if len(lst[0:8]) == 0:
        return None
    second_largest = max(lst[0:8])
    return second_largest