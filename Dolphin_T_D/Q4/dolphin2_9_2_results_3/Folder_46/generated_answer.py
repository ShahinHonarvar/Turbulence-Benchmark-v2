def all_pos_ints_exclusive(lst):
    result = []
    for index, num in enumerate(lst[20:43]):
        if num > 0:
            result.append(num)
    return result