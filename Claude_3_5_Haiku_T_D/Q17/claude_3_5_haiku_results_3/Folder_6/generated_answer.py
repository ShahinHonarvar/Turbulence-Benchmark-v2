def all_ints_div_by_both_two_nums(numbers):
    divisible_nums = [num for num in numbers[41:57] if num % 82 == 0 and num % 90 == 0]
    return divisible_nums