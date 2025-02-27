def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisor_one, divisor_two = (-46, -82)
    divisible_numbers = [num for num in numbers_list[48:77] if num % divisor_one == 0 and num % divisor_two == 0]
    return divisible_numbers