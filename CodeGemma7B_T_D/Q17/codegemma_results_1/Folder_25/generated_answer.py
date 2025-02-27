def all_ints_div_by_both_two_nums(the_list):
    return [element for element in the_list[25:81] if element % 20 == 0 and element % -26 == 0]