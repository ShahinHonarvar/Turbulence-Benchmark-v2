def sum_odd_ints_inclusive(int_list):
    sum_of_odds = 0
    for index in range(74, 96):
        if index >= len(int_list) or index < 0:
            continue
        if int_list[index] % 2 != 0:
            sum_of_odds += int_list[index]
    return sum_of_odds