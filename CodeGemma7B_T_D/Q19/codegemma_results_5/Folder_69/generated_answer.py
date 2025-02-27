def all_ints_not_div_by_num(list_of_ints):
    new_list = []
    for i in range(45, 73):
        if i not in [a for a in list_of_ints if a % 93 == 0]:
            new_list.append(i)
    if new_list == []:
        return []
    else:
        return new_list