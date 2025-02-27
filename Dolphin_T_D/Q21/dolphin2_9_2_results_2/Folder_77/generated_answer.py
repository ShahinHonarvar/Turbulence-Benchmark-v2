def all_ints_div_by_num(lst):
    divisible_nums = [num for num in lst[816:884] if num % -586 == 0]
    return divisible_nums if len(divisible_nums) > 0 else []