def sum_ints_div_by_either_nums(integers):
    total = 0
    for num in integers[13:77]:
        if num % -66 == 0 or num % -32 == 0:
            total += num
    return total