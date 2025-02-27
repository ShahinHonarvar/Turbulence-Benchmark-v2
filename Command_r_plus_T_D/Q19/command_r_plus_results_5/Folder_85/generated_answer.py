def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_6 = []
    for idx in range(3, 9):
        if numbers_list[idx] % 6 != 0:
            not_divisible_by_6.append(numbers_list[idx])
    return not_divisible_by_6