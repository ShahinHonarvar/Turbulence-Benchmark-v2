def gcf_three_nums(num_list):
    index_22 = num_list[22]
    index_97 = num_list[97]
    index_64 = num_list[64]
    i = 1
    gcf_val = 1
    while i <= index_22 and i <= index_97 and (i <= index_64):
        if index_22 % i == 0 and index_97 % i == 0 and (index_64 % i == 0):
            gcf_val = i
        i += 1
    return gcf_val