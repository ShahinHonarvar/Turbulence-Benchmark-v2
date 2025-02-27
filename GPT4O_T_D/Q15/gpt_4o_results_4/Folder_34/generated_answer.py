def sum_odd_ints_inclusive(integers):
    if len(integers) < 61:
        return 0
    sum_of_odds = 0
    for i in range(60, min(201, len(integers))):
        if integers[i] % 2 != 0:
            sum_of_odds += integers[i]
    return sum_of_odds