def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_68 = []
    for i in range(29, 53):
        if i < len(numbers_list) and numbers_list[i] % -68 != 0:
            not_divisible_by_68.append(numbers_list[i])
    return not_divisible_by_68