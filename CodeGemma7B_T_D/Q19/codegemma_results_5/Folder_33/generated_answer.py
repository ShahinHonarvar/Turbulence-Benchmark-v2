def all_ints_not_div_by_num(num_list):
    result = []
    for n in num_list[103:574]:
        if n % -514 != 0:
            result.append(n)
    return result