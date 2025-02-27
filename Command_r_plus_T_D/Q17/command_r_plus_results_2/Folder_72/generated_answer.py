def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-61, -71)
    divisible_by_both = [num for num in int_list[38:82] if num % divisor_1 == 0 and num % divisor_2 == 0]
    return divisible_by_both