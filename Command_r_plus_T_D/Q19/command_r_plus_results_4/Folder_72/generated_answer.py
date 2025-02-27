def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_78 = []
    for i in range(13, 70):
        if numbers_list[i] % -78 != 0:
            not_divisible_by_78.append(numbers_list[i])
    return not_divisible_by_78