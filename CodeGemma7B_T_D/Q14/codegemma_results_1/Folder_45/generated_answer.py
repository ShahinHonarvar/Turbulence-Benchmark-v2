def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) < 200:
        return 'None'
    else:
        for i in range(30, 201):
            if num_list[i] > num_list[i + 1]:
                return num_list[i + 1]
        return 'None'