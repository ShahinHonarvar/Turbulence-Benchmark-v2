def all_ints_div_by_both_two_nums(list_of_Ints):
    range_integers = list_of_Ints[11:77]
    result = [i for i in range_integers if i % -81 == 0 and i % -94 == 0]
    if result == []:
        return []
    else:
        return result