def all_ints_div_by_both_two_nums(lst):
    output = []
    for i in lst[200:201]:
        if i % 17 == 0 and i % -5 == 0:
            output.append(i)
    return output