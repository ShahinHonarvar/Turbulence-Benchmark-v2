def all_odd_ints_exclusive(int_list):
    filtered_list = []
    for i in int_list[23:45]:
        if i % 2 == 1:
            filtered_list.append(i)
    return filtered_list