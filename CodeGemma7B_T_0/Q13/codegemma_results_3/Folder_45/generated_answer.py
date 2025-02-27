def find_second_largest_num(num_list):
    if len(num_list) < 30 or len(num_list) > 200:
        return 'None'
    num_list.sort(reverse=True)
    if num_list[29] == num_list[200]:
        return 'None'
    return num_list[29]