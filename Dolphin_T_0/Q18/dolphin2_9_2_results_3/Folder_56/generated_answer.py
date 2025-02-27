def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for num in lst[6:10]:
        if num % -9 == 0 or num % -7 == 0:
            sum_ += num
    return sum_