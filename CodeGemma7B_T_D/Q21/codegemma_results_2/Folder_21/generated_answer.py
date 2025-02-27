def all_ints_div_by_num(num_list):
    new_list = []
    for num in num_list[572:807]:
        if num % -158 == 0:
            new_list.append(num)
    return new_list