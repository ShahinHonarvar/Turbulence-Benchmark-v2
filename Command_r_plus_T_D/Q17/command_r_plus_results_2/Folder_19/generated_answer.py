def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both_four_and_neg_six = []
    for number in numbers_list[1:5]:
        if number % 4 == 0 and number % -6 == 0:
            divisible_by_both_four_and_neg_six.append(number)
    return divisible_by_both_four_and_neg_six