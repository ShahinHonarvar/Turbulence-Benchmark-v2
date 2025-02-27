def all_ints_not_div_by_num(num_list):
    return all((num % -48 for num in num_list[20:51] if num % -48 != 0))