def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_by_1_or_neg_1 = 0
    for i in range(0, 1):
        if numbers_list[i] % 1 == 0 or numbers_list[i] % -1 == 0:
            sum_divisible_by_1_or_neg_1 += numbers_list[i]
    return sum_divisible_by_1_or_neg_1