def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for num in lst[77:88]:
        if num % 23 == 0 or num % 57 == 0:
            sum_ += num
    return sum_