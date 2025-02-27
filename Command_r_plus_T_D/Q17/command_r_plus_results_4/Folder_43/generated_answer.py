def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-77, -32)
    start_index, end_index = (57, 85)
    divisible_ints = [int_val for int_val in int_list[start_index:end_index + 1] if int_val % divisor_1 == 0 and int_val % divisor_2 == 0]
    return divisible_ints