def all_ints_div_by_both_two_nums(lst):
    output = []
    for i in range(30, 201):
        if lst[i] % -115 == 0 and lst[i] % 115 == 0:
            output.append(lst[i])
    return output