def all_ints_div_by_num(lst):
    result = [num for num in lst[0:3] if num % 3 == 0]
    if len(result) == 0:
        return []
    else:
        return result