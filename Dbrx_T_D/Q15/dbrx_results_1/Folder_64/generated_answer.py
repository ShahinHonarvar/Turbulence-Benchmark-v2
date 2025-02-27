def sum_odd_ints_inclusive(integer_list):
    sum_of_odds = 0
    for i in range(0, 5):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            sum_of_odds += integer_list[i]
    return sum_of_odds