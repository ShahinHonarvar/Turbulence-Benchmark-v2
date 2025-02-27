def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_27 = []
    for i in range(36, 85):
        if numbers_list[i] % -27 != 0:
            not_divisible_by_27.append(numbers_list[i])
    return not_divisible_by_27