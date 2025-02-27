def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[0:10] if i % 10 == 0 and i % 100 == 0]
    if len(result) == 0:
        return []
    else:
        return result