def all_ints_div_by_num(num_list):
    divisible_list = [num for num in num_list[40:69] if num % 16 == 0]
    if not divisible_list:
        return []
    return divisible_list