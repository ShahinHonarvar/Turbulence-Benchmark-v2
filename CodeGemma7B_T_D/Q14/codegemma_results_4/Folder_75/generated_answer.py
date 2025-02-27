def find_second_smallest_num(num_list):
    try:
        num_list = num_list[12:93]
        num_list.sort()
        return num_list[1]
    except IndexError:
        return 'None'