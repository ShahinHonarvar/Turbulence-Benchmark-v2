def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(max(0, 57), min(len(lst), 86)):
        if lst[i] % -77 == 0 and lst[i] % -32 == 0:
            result.append(lst[i])
    return result