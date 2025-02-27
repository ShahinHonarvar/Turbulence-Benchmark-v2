def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 2:
        return []
    start = min(lst[0], lst[1])
    end = max(lst[0], lst[1])
    return [i for i in range(start, end + 1) if i % 2 == 0 and i % 1 == 0]