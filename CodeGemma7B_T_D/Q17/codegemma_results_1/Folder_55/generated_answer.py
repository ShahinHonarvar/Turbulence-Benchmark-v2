def all_ints_div_by_both_two_nums(num_list):
    new_list = []
    for num in num_list:
        if num % 100 == 0 and num % 10 == 0:
            new_list.append(num)
    return new_list