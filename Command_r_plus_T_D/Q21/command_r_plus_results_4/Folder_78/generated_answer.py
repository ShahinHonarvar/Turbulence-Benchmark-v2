def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    start_index = 57
    end_index = 67
    divisible_by_90 = [num for num in int_list[start_index:end_index + 1] if num % 90 == 0]
    return divisible_by_90