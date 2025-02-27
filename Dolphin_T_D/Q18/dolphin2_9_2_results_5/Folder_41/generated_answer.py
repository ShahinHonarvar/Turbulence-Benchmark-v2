def sum_ints_div_by_either_nums(lst):
    sum_val = 0
    for num in lst[0:10]:
        if num % 6 == 0 or num % -3 == 0:
            sum_val += num
    return sum_val if sum_val != 0 else 0