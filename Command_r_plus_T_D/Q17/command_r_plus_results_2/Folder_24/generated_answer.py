def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(29, 54):
        if numbers_list[i] % -68 == 0 and numbers_list[i] % -85 == 0:
            divisible_by_both.append(numbers_list[i])
    return divisible_by_both