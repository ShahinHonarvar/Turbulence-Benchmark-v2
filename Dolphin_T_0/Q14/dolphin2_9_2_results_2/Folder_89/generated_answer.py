def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    elif 62 >= len(lst):
        return None
    min_num_1 = min(lst[62:63])
    min_num_2 = 'None'
    for i in lst[62:63]:
        if i < min_num_1 and i != min_num_2:
            min_num_2 = i
    if min_num_2 == 'None':
        return None
    else:
        return min_num_2