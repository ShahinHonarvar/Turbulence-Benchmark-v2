def all_ints_div_by_both_two_nums(list_of_ints):
    ints_div_by_both_two_nums = []
    for i in range(48, 77):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -46 == 0 and list_of_ints[i] % -82 == 0:
            ints_div_by_both_two_nums.append(list_of_ints[i])
    return ints_div_by_both_two_nums