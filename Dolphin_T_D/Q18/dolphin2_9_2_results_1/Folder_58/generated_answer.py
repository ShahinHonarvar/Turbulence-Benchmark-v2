def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[240:902]:
        if num % 546 == 0 or num % 709 == 0:
            total += num
    return total if total else 0