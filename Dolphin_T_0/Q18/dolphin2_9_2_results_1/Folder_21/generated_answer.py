def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for num in lst[315:935]:
        if num % -897 == 0 or num % -556 == 0:
            sum_ += num
    return sum_