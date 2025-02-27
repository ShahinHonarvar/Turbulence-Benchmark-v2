def all_ints_div_by_num(lst):
    result = [num for num in lst[32:36] if num % 91 == 0]
    return result if result else []