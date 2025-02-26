def all_ints_div_by_num(integer_list):
    start_index = 30
    end_index = 301
    return [num for num in integer_list[start_index:end_index] if num % 5 == 0]