def all_odd_ints_inclusive(int_list):
    odds_list = []
    if len(int_list) < 98:
        return odds_list
    for i in range(21, 98):
        if int_list[i] % 2 != 0:
            odds_list.append(int_list[i])
    return odds_list