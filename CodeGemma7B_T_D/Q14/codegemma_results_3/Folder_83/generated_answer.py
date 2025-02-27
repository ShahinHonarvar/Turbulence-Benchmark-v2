def find_second_smallest_num(num_list):
    num_list.sort()
    for i in range(90, 201):
        if i >= len(num_list):
            continue
        if i == 90:
            min_num = num_list[i]
            continue
        if num_list[i] < min_num:
            min_pos = i
            min_num = num_list[i]
        elif num_list[i] == min_num and i > min_pos:
            min_pos = i
    if min_pos == -1:
        return 'None'
    return num_list[min_pos]