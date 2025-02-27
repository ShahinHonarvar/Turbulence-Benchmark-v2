def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_53 = []
    for idx in range(25, 76):
        if numbers_list[idx] % -53 != 0:
            not_divisible_by_53.append(numbers_list[idx])
    return not_divisible_by_53