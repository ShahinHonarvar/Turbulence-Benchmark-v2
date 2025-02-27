def find_second_smallest_num(num_list):
    if len(num_list) <= 20 or len(num_list) >= 30:
        return 'None'
    num_list = sorted(num_list[20:31])
    return num_list[1]