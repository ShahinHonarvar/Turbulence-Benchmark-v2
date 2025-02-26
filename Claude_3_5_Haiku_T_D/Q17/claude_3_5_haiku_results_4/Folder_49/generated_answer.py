def all_ints_div_by_both_two_nums(input_list):
    return [num for num in input_list[80:201] if num % 10 == 0 and num % 1000 == 0]