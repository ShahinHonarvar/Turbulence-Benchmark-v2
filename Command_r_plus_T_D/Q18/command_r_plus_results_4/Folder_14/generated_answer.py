def sum_ints_div_by_either_nums(lst):
    if len(lst) > 9:
        divisible_nums = [num for num in lst[7:10] if num % 2 == 0 or num % 3 == 0]
        return sum(divisible_nums)
    return 0