def all_pos_ints_exclusive(lst):
    result = []
    for num in lst:
        if abs(num) < 0.5:
            if num > 69 and num < 200:
                result.append(num)
    return result