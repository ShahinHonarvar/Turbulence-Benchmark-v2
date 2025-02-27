def all_ints_div_by_num(lst):
    output = []
    for item in lst[62:64]:
        if item % 99 == 0:
            output.append(item)
    return output