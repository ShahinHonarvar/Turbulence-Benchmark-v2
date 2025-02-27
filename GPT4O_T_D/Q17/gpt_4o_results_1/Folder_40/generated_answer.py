def all_ints_div_by_both_two_nums(lst):
    if not lst or len(lst) < 2:
        return []
    start, end = (lst[0], lst[1])
    divisible_ints = []
    for i in range(start, end + 1):
        if i % 2 == 0 and i % 1 == 0:
            divisible_ints.append(i)
    return divisible_ints