def all_odd_ints_inclusive(int_list):
    odds = []
    for i in range(min(len(int_list), 66), min(len(int_list), 94)):
        if int_list[i] % 2 != 0:
            odds.append(int_list[i])
    return odds