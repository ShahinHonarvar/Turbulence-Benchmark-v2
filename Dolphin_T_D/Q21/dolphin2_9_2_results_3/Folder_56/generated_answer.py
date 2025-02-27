def all_ints_div_by_num(lst):
    result = [num for num in lst[:6] if num % 6 == 0]
    return result