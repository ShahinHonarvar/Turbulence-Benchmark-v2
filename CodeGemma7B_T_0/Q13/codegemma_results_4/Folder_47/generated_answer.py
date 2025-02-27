def find_second_largest_num(num_list):
    if len(num_list) < 38 or len(num_list) > 77:
        return 'None'
    num_list.sort(reverse=True)
    if num_list[37] == num_list[36]:
        return 'None'
    return num_list[37]