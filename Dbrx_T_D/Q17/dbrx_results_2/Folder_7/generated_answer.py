def all_ints_div_by_both_two_nums(lst):
    start_index = 543
    end_index = 584
    result = []
    for i in range(start_index, end_index + 1):
        if i < len(lst) and lst[i] % -553 == 0 and (lst[i] % -737 == 0):
            result.append(lst[i])
    return result