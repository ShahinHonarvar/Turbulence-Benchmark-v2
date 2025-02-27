def all_ints_div_by_num(integer_list):
    divisible_by_16 = [num for num in integer_list[40:69] if num % 16 == 0]
    return divisible_by_16