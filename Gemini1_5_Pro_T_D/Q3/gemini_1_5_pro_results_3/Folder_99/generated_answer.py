def all_pos_ints_inclusive(lst):
    result = []
    for i in range(max(0, min(310, len(lst) - 1)), min(371, len(lst))):
        if lst[i] > 0:
            result.append(lst[i])
    return result