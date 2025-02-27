def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 20 or len(num_list) > 200:
        return 'None'
    num_list.sort()
    if len(num_list) < 21:
        return num_list[1]
    for i in range(20, 201):
        if i < len(num_list):
            if num_list[i] > num_list[i - 1]:
                return num_list[i - 1]
    return 'None'