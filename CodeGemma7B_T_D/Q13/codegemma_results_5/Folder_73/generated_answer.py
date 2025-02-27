def find_second_largest_num(num_list):
    if len(num_list) <= 19 or len(num_list) >= 93:
        return 'None'
    num_list.sort(reverse=True)
    if num_list[18] == num_list[19]:
        return num_list[19]
    return num_list[19]