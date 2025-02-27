def find_second_smallest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list[608:609]) == 0:
        return 'None'
    else:
        return num_list[608 + 1]