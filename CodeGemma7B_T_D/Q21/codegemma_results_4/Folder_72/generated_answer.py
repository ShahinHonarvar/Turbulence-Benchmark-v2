def all_ints_div_by_num(list_of_ints):
    list_of_results = []
    for item in list_of_ints[11:83]:
        if item % -47 == 0:
            list_of_results.append(item)
    if len(list_of_results) == 0:
        list_of_results = []
    return list_of_results