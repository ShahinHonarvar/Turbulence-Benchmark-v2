def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) <= 30:
        return 0
    start_index = 30
    end_index = min(200, len(lst) - 1)
    return sum((x for x in lst[start_index:end_index + 1] if x % 115 == 0))