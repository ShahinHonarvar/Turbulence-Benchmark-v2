def sum_ints_div_by_either_nums(lst):
    total = 0
    for number in lst[93:95]:
        if number % -53 == 0 or number % -91 == 0:
            total += number
    return total