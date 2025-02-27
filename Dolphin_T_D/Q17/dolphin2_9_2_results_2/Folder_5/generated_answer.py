def all_ints_div_by_both_two_nums(lst):
    divisible_nums = lst[0:2]
    result = []
    for num in divisible_nums:
        if num % -6 == 0 and num % 4 == 0:
            result.append(num)
    return result