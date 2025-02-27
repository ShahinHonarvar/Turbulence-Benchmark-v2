def sum_ints_div_by_either_nums(int_list):
    filtered_ints = [num for num in int_list[13:92] if num % -65 == 0 or num % -62 == 0]
    return sum(filtered_ints)