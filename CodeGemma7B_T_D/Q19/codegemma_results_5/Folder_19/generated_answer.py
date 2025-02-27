def all_ints_not_div_by_num(list_ints):
    new_list = []
    for num in list_ints[4:5]:
        if num % 7 != 0:
            new_list.append(num)
    return new_list