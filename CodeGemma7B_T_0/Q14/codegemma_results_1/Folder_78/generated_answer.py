def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 17 or len(num_list) > 78:
        return 'None'
    num_list = num_list[16:79]
    num_list.sort()
    return num_list[1]