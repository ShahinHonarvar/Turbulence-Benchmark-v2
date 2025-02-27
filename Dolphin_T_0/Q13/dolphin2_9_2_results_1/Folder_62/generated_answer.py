def find_second_largest_num(lst):
    if lst[91:100]:
        return sorted(lst)[-2] if len(lst) > 1 else None
    else:
        return None