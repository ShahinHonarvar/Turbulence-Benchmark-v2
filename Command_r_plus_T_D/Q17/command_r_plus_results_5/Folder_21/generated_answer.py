def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-897, -556)
    divisible_by_both = []
    for index, number in enumerate(numbers_list[314:935], start=315):
        if number % divisor_1 == 0 and number % divisor_2 == 0:
            divisible_by_both.append(number)
    return divisible_by_both