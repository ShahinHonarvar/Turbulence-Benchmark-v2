def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 201 or max(num_list) - min(num_list) < 200:
        return 'None'
    num_list = sorted(num_list[40:201])
    return num_list[1]