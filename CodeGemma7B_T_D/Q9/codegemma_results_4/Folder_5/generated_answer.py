def all_odd_ints_inclusive(num_list):
    num_list = num_list[8:10]
    temp_list = []
    for i in num_list:
        if i % 2 != 0:
            temp_list.append(i)
    return temp_list