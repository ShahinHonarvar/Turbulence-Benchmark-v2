def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both_8_and_neg_3 = []
    for num in numbers_list[:5]:
        if num % 8 == 0 and num % -3 == 0:
            divisible_by_both_8_and_neg_3.append(num)
    return divisible_by_both_8_and_neg_3