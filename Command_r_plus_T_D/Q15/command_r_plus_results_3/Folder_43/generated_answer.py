def sum_odd_ints_inclusive(numbers_list):
    sum_odds = 0
    for index in range(68, 87):
        if numbers_list[index] % 2 != 0:
            sum_odds += numbers_list[index]
    return sum_odds