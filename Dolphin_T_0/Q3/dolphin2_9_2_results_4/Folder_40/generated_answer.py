def all_pos_ints_inclusive(lst):
    result = []
    for number in lst[0:2]:
        if number > 0:
            result.append(number)
    return result