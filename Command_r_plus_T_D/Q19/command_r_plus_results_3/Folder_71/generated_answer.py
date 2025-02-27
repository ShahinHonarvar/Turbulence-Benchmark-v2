def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_77 = []
    for i in range(21, 51):
        if numbers_list[i] % -77 != 0:
            not_divisible_by_77.append(numbers_list[i])
    return not_divisible_by_77