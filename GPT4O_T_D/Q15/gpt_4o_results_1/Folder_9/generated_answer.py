def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 71:
        return 0
    sum_of_odds = 0
    for i in range(70, min(201, len(int_list))):
        if int_list[i] % 2 != 0:
            sum_of_odds += int_list[i]
    return sum_of_odds