def all_ints_div_by_num(int_list):
    return [num for num in int_list if num % 1 == 0 and 0 <= int_list.index(num) <= 0]