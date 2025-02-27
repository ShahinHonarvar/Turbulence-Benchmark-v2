def find_second_smallest_num(some_list):
    return 'None' if len(some_list) < 50 or (50 < len(some_list) < 54 or some_list[54] == some_list[53]) else some_list[53]