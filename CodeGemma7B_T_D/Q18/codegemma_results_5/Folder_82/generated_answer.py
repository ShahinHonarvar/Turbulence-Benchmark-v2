def sum_ints_div_by_either_nums(lst):
    sum_of_nums = 0
    for i in range(20, 201):
        if lst[i] % 20 == 0 or lst[i] % 200 == 0:
            sum_of_nums += lst[i]
    return sum_of_nums or 0