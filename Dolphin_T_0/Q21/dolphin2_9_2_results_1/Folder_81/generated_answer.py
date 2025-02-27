def all_ints_div_by_num(lst):
    result = [i for i in lst[:3] if i % 5 == 0]
    return result if result else []