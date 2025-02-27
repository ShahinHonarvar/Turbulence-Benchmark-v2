def sum_odd_ints_inclusive(numbers_list):
    sum_odds = 0
    for i in range(6, len(numbers_list)):
        if numbers_list[i] % 2 != 0:
            sum_odds += numbers_list[i]
    return sum_odds