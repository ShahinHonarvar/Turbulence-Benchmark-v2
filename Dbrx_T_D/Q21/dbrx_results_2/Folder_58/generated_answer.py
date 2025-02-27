def all_ints_div_by_num(num_list):
    start_index = 255
    end_index = 618
    result = []
    for i in range(len(num_list)):
        if i >= start_index and i <= end_index:
            if num_list[i] % 965 == 0:
                result.append(num_list[i])
    return result