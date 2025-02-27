def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(81, 90):
        if numbers_list[i] % 56 == 0 and numbers_list[i] % 68 == 0:
            divisible_by_both.append(numbers_list[i])
    return divisible_by_both