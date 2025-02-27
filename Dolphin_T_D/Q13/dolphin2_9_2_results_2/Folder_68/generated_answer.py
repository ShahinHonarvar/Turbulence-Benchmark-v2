def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    else:
        first_largest = max(lst[:9])
        lst.remove(first_largest)
        return max(lst[:9])