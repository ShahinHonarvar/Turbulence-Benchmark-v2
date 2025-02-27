def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) < 22 or num_list[21] == num_list[-1]:
        return 'None'
    else:
        return num_list[21]