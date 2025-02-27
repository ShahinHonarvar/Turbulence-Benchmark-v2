def all_pos_ints_inclusive(lst):
    result = []
    for num in lst:
        if 91 <= num <= 99 and num > 0:
            result.append(num)
    return result