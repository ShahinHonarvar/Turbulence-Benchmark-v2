def all_ints_div_by_both_two_nums(lst):
    start_index = 29
    end_index = 53
    divisibles = []
    for i in range(start_index, min(end_index + 1, len(lst))):
        if lst[i] % -68 == 0 and lst[i] % -85 == 0:
            divisibles.append(lst[i])
    return divisibles