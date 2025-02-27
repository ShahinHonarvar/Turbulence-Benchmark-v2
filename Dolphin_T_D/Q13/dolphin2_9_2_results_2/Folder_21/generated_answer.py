def find_second_largest_num(my_list):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return None
    max_num = max(my_list[639:976])
    second_max_num = float('-inf')
    for index in range(639, 976):
        if max_num > my_list[index] > second_max_num:
            second_max_num = my_list[index]
    if second_max_num != float('-inf'):
        return second_max_num
    else:
        return None