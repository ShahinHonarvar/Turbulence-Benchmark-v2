def all_ints_div_by_num(lst):
    result = [num for num in lst[0:1] if num % 9 == 0]
    if len(result) == 0:
        return []
    else:
        return result