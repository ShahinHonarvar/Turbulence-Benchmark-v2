def all_ints_not_div_by_num(lst):
    result = [num for num in lst[31:69] if num % -70 != 0]
    return result if result else []