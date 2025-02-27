def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[299:383]:
        if num % 858 == 0 or num % 952 == 0:
            total += num
    return total