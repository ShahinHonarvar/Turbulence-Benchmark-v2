def all_ints_div_by_num(num_list: list[int]) -> list[int]:
    start_index = 574
    end_index = 744
    divisible_by_649 = [num for num in num_list[start_index:end_index + 1] if num % 649 == 0]
    return divisible_by_649