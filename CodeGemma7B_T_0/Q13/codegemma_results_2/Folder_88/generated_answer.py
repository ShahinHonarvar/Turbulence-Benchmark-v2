def find_second_largest_num(num_list):
    if len(num_list) < 5 or len(num_list) > 9:
        return 'None'
    num_list.sort()
    if num_list[-2] < num_list[-5]:
        return 'None'
    return num_list[-2]