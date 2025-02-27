def sum_ints_div_by_either_nums(lst):
    sum = 0
    slice_lst = lst[69:71]
    for num in slice_lst:
        if num % 72 == 0 or num % 70 == 0:
            sum += num
    return sum if sum != 0 else 0