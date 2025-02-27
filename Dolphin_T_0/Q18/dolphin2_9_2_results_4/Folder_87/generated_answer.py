def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[18:53]:
        if num % 15 == 0 or num % 57 == 0:
            total += num
    return total if total != 0 else 0