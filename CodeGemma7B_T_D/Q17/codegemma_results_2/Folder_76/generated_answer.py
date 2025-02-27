def all_ints_div_by_both_two_nums(some_list):
    filtered_list = []
    for num in some_list[250:630]:
        if num % 850 == 0 and num % 587 == 0:
            filtered_list.append(num)
    return filtered_list