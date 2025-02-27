def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both_six_and_neg_three = []
    for num in numbers_list[0:10]:
        if num % 6 == 0 and num % -3 == 0:
            divisible_by_both_six_and_neg_three.append(num)
    return divisible_by_both_six_and_neg_three