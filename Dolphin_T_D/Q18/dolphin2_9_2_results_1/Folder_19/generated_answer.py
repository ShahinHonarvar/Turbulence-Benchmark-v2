def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(1, 5):
        if i % 4 == 0 or i % -6 == 0:
            sum += i
    return sum