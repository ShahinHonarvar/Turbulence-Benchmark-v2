def all_ints_not_div_by_num(lst):
    result = [i for i in lst[15:92] if i % 59 != 0]
    return result if result else []