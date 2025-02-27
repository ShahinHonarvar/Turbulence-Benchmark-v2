def all_ints_not_div_by_num(num_list):
    new_list = []
    for num in num_list[40:200]:
        if num % num_list[0] != 71:
            new_list.append(num)
    if new_list == []:
        return new_list
    else:
        return new_list