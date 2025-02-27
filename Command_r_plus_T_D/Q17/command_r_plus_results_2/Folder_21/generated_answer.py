def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-897, -556)
    divisible_by_both = []
    for i in range(315, 935):
        if numbers_list[i] % divisor_1 == 0 and numbers_list[i] % divisor_2 == 0:
            divisible_by_both.append(numbers_list[i])
    return divisible_by_both