def all_odd_ints_exclusive(int_list):
    odds = []
    for i in range(111, 473):
        num = int_list[i]
        if num % 2 != 0:
            odds.append(num)
    return odds