def find_second_smallest_num(lst):
    if 17 <= len(lst) <= 78:
        sliced = lst[17:79]
        sorted_sliced = sorted(sliced)
        if len(sorted_sliced) >= 2:
            return sorted_sliced[1]
        else:
            return None
    else:
        return None