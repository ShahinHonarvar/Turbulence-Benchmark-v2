def all_ints_div_by_both_two_nums(lst):
    answer = [x for x in lst[55:81] if x % 22 == 0 and x % 32 == 0]
    return answer if answer else []