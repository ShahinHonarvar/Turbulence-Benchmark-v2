def all_ints_not_div_by_num(lst):
    num = -1
    start = 0
    end = 1
    result = [i for i in lst[start:end] if i % num != 0]
    return result