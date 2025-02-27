def all_ints_div_by_num(lst):
    divisible_by_39 = [lst[i] for i in range(30, 60) if lst[i] % 39 == 0]
    return divisible_by_39 if divisible_by_39 else []