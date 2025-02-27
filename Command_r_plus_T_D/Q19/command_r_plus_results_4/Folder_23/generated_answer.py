def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_num = []
    for i in range(44, 91):
        if numbers_list[i] % -68 != 0:
            not_divisible_by_num.append(numbers_list[i])
    return not_divisible_by_num