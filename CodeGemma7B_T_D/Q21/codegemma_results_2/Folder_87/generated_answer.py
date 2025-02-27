def all_ints_div_by_num(int_list):
    new_list = []
    for num in int_list[10:57]:
        if num % 16 == 0:
            new_list.append(num)
    return new_list if new_list else []