def find_second_smallest_num(num_list):
    num_list_s = sorted(num_list)
    if len(num_list_s) < 31 or len(num_list_s) > 88:
        return 'None'
    else:
        return num_list_s[30]