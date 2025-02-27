def sum_ints_div_by_either_nums(lst):
    total = 0
    for number in lst[57:82]:
        if number % 55 == 0 or number % 10 == 0:
            total += number
    return total