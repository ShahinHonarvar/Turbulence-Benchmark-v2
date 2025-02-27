def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[250:630]:
        if num % 850 == 0 or num % 587 == 0:
            total += num
    return total