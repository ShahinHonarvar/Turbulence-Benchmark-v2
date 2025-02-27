def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_10_and_100 = []
    for i in range(10, 101):
        if numbers_list[i] % 10 == 0 and numbers_list[i] % 100 == 0:
            divisible_by_10_and_100.append(numbers_list[i])
    return divisible_by_10_and_100