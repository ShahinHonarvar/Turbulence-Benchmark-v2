def sum_ints_div_by_either_nums(lst):
    start_index = 200
    end_index = 200
    sum_divisible = 0
    for i in range(start_index, end_index + 1):
        if lst[i] % 17 == 0 or lst[i] % -5 == 0:
            sum_divisible += lst[i]
    return sum_divisible