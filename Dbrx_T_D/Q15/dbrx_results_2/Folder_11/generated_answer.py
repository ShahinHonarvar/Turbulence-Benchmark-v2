def sum_odd_ints_inclusive(lst):
    slice_lst = lst[36:52]
    result = 0
    for num in slice_lst:
        if num % 2 != 0:
            result += num
    return result