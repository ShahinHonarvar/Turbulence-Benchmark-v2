def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(42, 88):
        num = int_list[i]
        if num % 90 == 0 or num % 74 == 0:
            sum += num
    return sum or 0