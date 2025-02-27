def all_ints_div_by_num(lst):
    result = lst[11:83]
    result = [num for num in result if num % -47 == 0]
    return result