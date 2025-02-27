def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 51:
        return 0
    return sum((num for num in int_list[31:51] if num % 81 == 0 or num % 64 == 0))