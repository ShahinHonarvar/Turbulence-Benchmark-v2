def sum_ints_div_by_either_nums(ls):
    total = 0
    for num in ls[56:89]:
        if num % -59 == 0 or num % -79 == 0:
            total += num
    return total if total != 0 else 0