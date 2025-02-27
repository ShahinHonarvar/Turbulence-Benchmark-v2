def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(48, 60):
        if numbers_list[i] % 88 == 0 and numbers_list[i] % 58 == 0:
            divisible_by_both.append(numbers_list[i])
    return divisible_by_both