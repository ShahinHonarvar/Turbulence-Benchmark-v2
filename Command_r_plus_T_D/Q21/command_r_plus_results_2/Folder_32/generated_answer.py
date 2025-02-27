def all_ints_div_by_num(num_list: list[int]) -> list[int]:
    div_by_31 = [num for num in num_list[38:56] if num % 31 == 0]
    return div_by_31