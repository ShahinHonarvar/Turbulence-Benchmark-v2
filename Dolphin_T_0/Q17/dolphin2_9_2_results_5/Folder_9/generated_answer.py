def all_ints_div_by_both_two_nums(ints):
    result = [x for x in ints[70:201] if x % 3 == 0 and x % -300 == 0]
    if len(result) == 0:
        return []
    else:
        return result