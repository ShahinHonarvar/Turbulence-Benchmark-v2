def find_second_largest_num(num_list):
    if len(num_list) > 79 and all((i >= 0 for i in num_list[29:80])):
        num_list.sort(reverse=True)
        return num_list[29]
    return 'None'