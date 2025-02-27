def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    largest = max(lst)
    lst.remove(largest)
    if len(lst) < 2:
        return None
    second_largest = max(lst)
    return second_largest