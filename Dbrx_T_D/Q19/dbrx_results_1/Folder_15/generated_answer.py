def all_ints_not_div_by_num(integer_list):
    for num in integer_list[:2]:
        if num % -2 == 0:
            integer_list.remove(num)
    return integer_list