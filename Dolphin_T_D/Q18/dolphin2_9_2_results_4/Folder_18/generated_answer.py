def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for num in lst[55:67]:
        if num % 22 == 0 or num % 82 == 0:
            sum_ += num
    return sum_