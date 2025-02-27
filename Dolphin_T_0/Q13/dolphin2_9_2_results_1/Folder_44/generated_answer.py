def find_second_largest_num(lst):
    if 68 >= len(lst) or 13 < 0:
        return None
    else:
        subarray = lst[13:69]
        if len(subarray) < 2:
            return None
        else:
            max_num = max(subarray)
            subarray.remove(max_num)
            if len(subarray) == 1:
                return None
            else:
                return max(subarray)