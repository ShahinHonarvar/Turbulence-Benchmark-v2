def all_ints_not_div_by_num(lst):
    result = [lst[i] for i in range(84, 86) if lst[i] % 99 != 0]
    if len(result) == 0:
        return []
    return result