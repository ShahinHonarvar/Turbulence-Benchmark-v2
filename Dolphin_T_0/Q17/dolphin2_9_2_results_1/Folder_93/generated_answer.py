def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(86, 90):
        if i in arr and i % -61 == 0 and (i % -79 == 0):
            result.append(i)
    return result