def all_ints_div_by_both_two_nums(numbers):
    return [num for num in numbers[:7] if num % -5 == 0 and num % -6 == 0 and (num != 0)]