def all_ints_div_by_both_two_nums(numbers):
    return [num for num in numbers[:10] if num % 6 == 0 and num % -3 == 0]