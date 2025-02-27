def all_ints_div_by_num(lst):
    start = 6
    end = 8
    return [num for num in lst[start:end + 1] if num % -9 == 0] if len(lst[start:end + 1]) > 0 else []