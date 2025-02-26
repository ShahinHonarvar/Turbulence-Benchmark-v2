def all_ints_not_div_by_num(lst):
    if len(lst) < 96:
        return []
    result = [num for num in lst[94:94] if num % 57 != 0]
    return result