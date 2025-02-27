def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    sum_of_odds = 0
    for index in range(60, 201):
        if numbers_list[index] % 2 != 0:
            sum_of_odds += numbers_list[index]
    return sum_of_odds