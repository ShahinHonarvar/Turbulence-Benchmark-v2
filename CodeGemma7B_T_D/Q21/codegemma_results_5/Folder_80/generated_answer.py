def all_ints_div_by_num(int_list):
    output = []
    for num in int_list[27:88]:
        if num % 29 == 0:
            output.append(num)
    if output:
        return output
    else:
        return []