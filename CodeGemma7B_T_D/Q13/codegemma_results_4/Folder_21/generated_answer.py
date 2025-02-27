def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    for i in range(639, 976):
        if i < len(num_list):
            return num_list[i]
    return 'None'