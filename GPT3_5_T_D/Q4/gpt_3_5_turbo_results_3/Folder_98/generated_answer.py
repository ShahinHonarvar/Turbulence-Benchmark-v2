def all_pos_ints_exclusive(lst):
    result = []
    for num in lst[0:6]:
        if num > 0:
            result.append(num)
    return result