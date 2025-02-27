def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for i in range(51, 77):
        if numbers_list[i] % -90 == 0 and numbers_list[i] % -59 == 0:
            divisible_by_both.append(numbers_list[i])
    return divisible_by_both