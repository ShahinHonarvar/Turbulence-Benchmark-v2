def find_second_largest_num(lst):
    sublst = lst[91:100]
    if not sublst:
        return None
    else:
        max_num = max(sublst)
        sublst.remove(max_num)
        if not sublst:
            return None
        else:
            return max(sublst)