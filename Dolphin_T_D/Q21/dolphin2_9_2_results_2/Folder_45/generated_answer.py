def all_ints_div_by_num(int_list):
    divisible_ints = []
    for i in range(3):
        if i in int_list and i % 9 == 0:
            divisible_ints.append(i)
    return divisible_ints