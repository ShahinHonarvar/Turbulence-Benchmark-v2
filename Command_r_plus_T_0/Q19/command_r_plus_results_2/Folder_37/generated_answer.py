def all_ints_not_div_by_num(lst):
    result = [num for num in lst[1:-1] if num % 5 != 0]
    return result