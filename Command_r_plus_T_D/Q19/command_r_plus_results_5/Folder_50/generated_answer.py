def all_ints_not_div_by_num(num_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(num_list[13:76], 13) if num % 44 != 0]