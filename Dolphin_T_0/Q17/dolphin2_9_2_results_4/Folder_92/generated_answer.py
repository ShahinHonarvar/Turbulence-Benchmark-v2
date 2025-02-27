def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for num in lst[0:1]:
        if num % 1 == 0 and num % -1 == 0:
            divisible_by_both.append(num)
    return divisible_by_both