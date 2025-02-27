def find_second_largest_num(num_list):
    if num_list[6:9]:
        num_list[6:9].sort(reverse=True)
        return num_list[7]
    return 'None'