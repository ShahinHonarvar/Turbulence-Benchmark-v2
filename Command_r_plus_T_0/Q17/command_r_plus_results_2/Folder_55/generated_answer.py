def all_ints_div_by_both_two_nums(numbers_list):
    divisible_by_both = [num for num in numbers_list[:10] if num % 10 == 0 and num % 100 == 0]
    return divisible_by_both