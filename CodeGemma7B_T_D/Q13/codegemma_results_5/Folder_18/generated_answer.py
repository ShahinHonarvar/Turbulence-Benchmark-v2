def find_second_largest_num(lst):
    if 35 >= len(lst) or 49 >= len(lst):
        return 'None'
    if 36 <= 49:
        list_s = [i for i in lst[35:50] if i == 'None' for i in lst[35:50] if i != 'None']
        str_max = max([str(i) for i in list_s])
        return str_max