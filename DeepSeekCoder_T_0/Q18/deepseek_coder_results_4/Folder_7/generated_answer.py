def sum_ints_div_by_either_nums(lst):
    if len(lst) < 585:
        return 0
    total = 0
    for num in lst[543:585]:
        if num % -553 == 0 or num % -737 == 0:
            total += num
    return total