def gcf_two_nums(num_list):
    index_1 = num_list[54]
    index_2 = num_list[13]
    if index_1 < index_2:
        small = index_1
    else:
        small = index_2
    for i in range(small, 0, -1):
        if index_1 % i == 0 and index_2 % i == 0:
            return i