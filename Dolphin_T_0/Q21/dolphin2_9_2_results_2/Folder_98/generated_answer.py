def all_ints_div_by_num(lst):
    result = [num for num in lst if num % 6 == 0]
    return result if result else []