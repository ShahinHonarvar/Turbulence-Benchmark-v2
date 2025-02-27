def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_85 = [num for num in int_list[18:94] if num % -85 == 0]
    return divisible_by_85