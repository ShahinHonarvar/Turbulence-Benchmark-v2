def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[31:51], start=31) if num % 81 == 0 or num % 64 == 0))