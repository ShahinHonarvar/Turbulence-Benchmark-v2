def all_ints_not_div_by_num(num_list, index1, index2):
    return [num for num in num_list[index1:index2] if num % 8 != 0]