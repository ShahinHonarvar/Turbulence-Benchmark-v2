def all_ints_div_by_both_two_nums(numbers):
    return [num for num in numbers[:6] if num % -1 == 0 and num % 13 == 0]