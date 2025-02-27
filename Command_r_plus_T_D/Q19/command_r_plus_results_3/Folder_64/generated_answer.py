def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_2 = []
    for i in range(2, len(numbers_list)):
        if numbers_list[i] % 2 != 0:
            not_divisible_by_2.append(numbers_list[i])
    return not_divisible_by_2