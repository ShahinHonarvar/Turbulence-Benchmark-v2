def all_ints_div_by_num(my_list):
    divisible_by_39 = [my_list[i] for i in range(30, 60) if my_list[i] % 39 == 0]
    return divisible_by_39 if len(divisible_by_39) > 0 else []