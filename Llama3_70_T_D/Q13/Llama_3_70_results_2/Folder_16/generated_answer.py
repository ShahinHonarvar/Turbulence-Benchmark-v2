def find_second_largest_num(lst):
    num_slice = lst[33:37]
    if len(num_slice) < 2:
        return None
    return sorted(set(num_slice), reverse=True)[1]