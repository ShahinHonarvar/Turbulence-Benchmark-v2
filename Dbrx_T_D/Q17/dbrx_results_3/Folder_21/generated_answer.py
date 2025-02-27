def all_ints_div_by_both_two_nums(lst):
    start, end = (315, 934)
    if not lst or not lst[start:end + 1]:
        return []
    result = []
    for i in lst[start:end + 1]:
        if i % -897 == 0 and i % -556 == 0:
            result.append(i)
    return result