def all_ints_div_by_num(lst):
    result = [num for num in lst[42:77] if num % 14 == 0]
    return result if result else []