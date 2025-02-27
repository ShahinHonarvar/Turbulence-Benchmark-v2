def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-90, -59)
    divisible_by_both = [num for num in numbers_list[51:77] if num % divisor_1 == 0 and num % divisor_2 == 0]
    return divisible_by_both