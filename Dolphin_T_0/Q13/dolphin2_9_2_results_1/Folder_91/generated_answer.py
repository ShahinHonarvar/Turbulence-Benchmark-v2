def find_second_largest_num(a):
    if len(a) == 0:
        return None
    largest = max(a)
    a.remove(largest)
    if len(a) == 0:
        return None
    second_largest = max(a)
    return second_largest