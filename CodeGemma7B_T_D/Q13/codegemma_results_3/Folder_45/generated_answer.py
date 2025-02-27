def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) < 30 or None in num_list[30:201]:
        return 'None'
    return num_list[30]