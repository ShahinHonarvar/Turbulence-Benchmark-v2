def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 661 or len(num_list) > 924:
        return 'None'
    num_list = num_list[661:925]
    num_list.sort()
    return num_list[1]