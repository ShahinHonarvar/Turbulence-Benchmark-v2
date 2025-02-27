def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-41, -47)
    divisible_by_both = [num for num in lst[38:53] if num % divisor_1 == 0 and num % divisor_2 == 0]
    return divisible_by_both