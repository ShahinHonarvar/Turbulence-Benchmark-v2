def all_ints_div_by_num(num_list):
    divisible_by_6 = [num for num in num_list[1:9] if num % 6 == 0]
    return divisible_by_6 if len(divisible_by_6) > 0 else []