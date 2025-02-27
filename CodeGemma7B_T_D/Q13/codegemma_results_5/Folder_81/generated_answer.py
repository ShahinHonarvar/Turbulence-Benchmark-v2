def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    try:
        return num_list[10:101][1]
    except IndexError:
        return 'None'