def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    start_index = 59
    end_index = 78
    divisible_by_num = -95
    divisible_ints = [int for int in int_list[start_index:end_index] if int % divisible_by_num == 0]
    return divisible_ints