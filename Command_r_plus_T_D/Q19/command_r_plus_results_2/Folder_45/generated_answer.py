def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_neg_115 = []
    for i in range(30, 200):
        if numbers_list[i] % -115 != 0:
            not_divisible_by_neg_115.append(numbers_list[i])
    return not_divisible_by_neg_115