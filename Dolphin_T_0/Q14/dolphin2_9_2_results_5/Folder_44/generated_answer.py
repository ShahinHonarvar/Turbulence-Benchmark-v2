def find_second_smallest_num(lst):
    if len(lst) >= 100:
        if len(set(lst[91:100])) > 1:
            return sorted(lst[91:100])[1]
    return None