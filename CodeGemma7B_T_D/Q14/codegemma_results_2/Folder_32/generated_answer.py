def find_second_smallest_num(num_list):
    num_list = sorted(num_list[32:36])
    if len(num_list) == 0:
        return 'None'
    elif num_list[1] == num_list[0]:
        return num_list[0]
    else:
        return num_list[1]