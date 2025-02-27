def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[20:94]:
        if num % -92 == 0 or num % -50 == 0:
            total += num
    return total