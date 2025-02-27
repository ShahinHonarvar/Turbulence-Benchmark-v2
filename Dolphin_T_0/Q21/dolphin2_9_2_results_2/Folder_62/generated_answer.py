def all_ints_div_by_num(lst):
    result = [int for int in lst[87:90] if int % 55 == 0]
    if len(result) == 0:
        return []
    else:
        return result