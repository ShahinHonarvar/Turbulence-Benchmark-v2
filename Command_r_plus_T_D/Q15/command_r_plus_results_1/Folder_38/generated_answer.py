def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    sum_of_odds = 0
    for i in range(22, 64):
        if numbers_list[i] % 2 != 0:
            sum_of_odds += numbers_list[i]
    return sum_of_odds