def all_ints_div_by_num(num_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(num_list[20:98]) if num % 46 == 0]