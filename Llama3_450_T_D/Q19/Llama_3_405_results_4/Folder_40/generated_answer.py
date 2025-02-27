def all_ints_not_div_by_num(lst):
    if len(lst) < 2:
        return []
    start = lst[0] + 1
    end = lst[1]
    return [i for i in range(start, end) if i % 1 != 0]