def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_neg_19 = [num for num in int_list[11:78] if num % -19 == 0]
    return divisible_by_neg_19