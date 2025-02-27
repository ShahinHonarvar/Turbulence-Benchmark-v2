def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 201 or max(num_list) - min(num_list) < 201:
        return 'None'
    num_list = sorted(num_list)
    for i in range(70, 201):
        if i < len(num_list):
            return num_list[i]
    return 'None'