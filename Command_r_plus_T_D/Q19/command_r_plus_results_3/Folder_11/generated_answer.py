def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_27 = []
    for idx in range(36, 85):
        if numbers_list[idx] % -27 != 0:
            not_divisible_by_27.append(numbers_list[idx])
    return not_divisible_by_27