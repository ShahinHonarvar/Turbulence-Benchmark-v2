def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-553, -737)
    start_index, end_index = (543, 584)
    divisible_ints = [int for int in int_list[start_index:end_index + 1] if int % divisor_1 == 0 and int % divisor_2 == 0]
    return divisible_ints