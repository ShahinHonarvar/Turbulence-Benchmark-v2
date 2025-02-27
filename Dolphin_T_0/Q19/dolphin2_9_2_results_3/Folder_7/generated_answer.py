def all_ints_not_div_by_num(int_list):
    desired_num = -201
    return [num for num in int_list[495:826] if num % desired_num != 0]