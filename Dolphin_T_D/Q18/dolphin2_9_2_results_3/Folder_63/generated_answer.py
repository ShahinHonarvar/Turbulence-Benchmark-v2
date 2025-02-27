def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(31, 51):
        num = lst[i]
        if num % 81 == 0 or num % 64 == 0:
            sum += num
    return sum