def find_second_smallest_num(lst):
    indices = [i for i in lst[1:9]]
    if len(indices) < 2:
        return None
    else:
        return sorted(indices)[1]