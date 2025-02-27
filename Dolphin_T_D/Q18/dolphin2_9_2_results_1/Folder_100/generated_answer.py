def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[72:94]:
        if num % 32 == 0 or num % 44 == 0:
            total += num
    return total if total != 0 else 0