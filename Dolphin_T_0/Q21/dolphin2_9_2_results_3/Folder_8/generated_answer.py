def all_ints_div_by_num(lst):
    result = [num for num in lst[34:56] if num % -83 == 0]
    if result:
        return result
    else:
        return []