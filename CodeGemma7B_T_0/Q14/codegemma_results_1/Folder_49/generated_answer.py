def find_second_smallest_num(num_list):
    num_list = num_list[80:201]
    num_list.sort()
    if len(num_list) < 2:
        return 'None'
    return num_list[1]