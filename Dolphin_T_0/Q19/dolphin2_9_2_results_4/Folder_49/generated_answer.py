def all_ints_not_div_by_num(lst):
    output = []
    for i in lst[80:200]:
        if i % 1000 != 0:
            output.append(i)
    return output