def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisor_one, divisor_two = (-553, -737)
    start_index, end_index = (543, 584)
    divisible_ints = [i for i in int_list[start_index:end_index + 1] if i % divisor_one == 0 and i % divisor_two == 0]
    return divisible_ints