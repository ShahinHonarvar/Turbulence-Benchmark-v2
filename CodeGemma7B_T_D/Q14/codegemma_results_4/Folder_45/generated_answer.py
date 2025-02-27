def find_second_smallest_num(num_lst):
    if len(num_lst) < 200:
        return 'None'
    num_lst = sorted(num_lst[30:201])
    return num_lst[1] if len(num_lst) >= 2 else 'None'