def all_pos_ints_inclusive(lst):
    result = []
    for number in lst[42:69]:
        if number >= 0:
            result.append(number)
    return result if result else []