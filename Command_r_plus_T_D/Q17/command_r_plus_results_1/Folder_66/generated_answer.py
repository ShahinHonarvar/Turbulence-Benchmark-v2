def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(58, 82):
        if numbers_list[i] % 55 == 0 and numbers_list[i] % 10 == 0:
            divisible_by_both.append(numbers_list[i])
    return divisible_by_both