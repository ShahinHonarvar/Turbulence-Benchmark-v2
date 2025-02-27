def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[281:695]:
        if num % -722 == 0 or num % -731 == 0:
            total += num
    return total