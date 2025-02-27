def all_pos_ints_inclusive(lst):
    result = []
    for i in range(max(10, 0), min(67, len(lst))):
        if lst[i] > 0:
            result.append(lst[i])
    return result