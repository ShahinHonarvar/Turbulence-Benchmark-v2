def all_ints_div_by_both_two_nums(numbers):
    return [num for num in numbers[:3] if num % -2 == 0 and num % 3 == 0]