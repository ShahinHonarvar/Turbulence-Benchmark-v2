def find_second_largest_num(num_list):
    try:
        if len(num_list) < 2:
            raise ValueError
        num_list.sort()
        return num_list[-2]
    except ValueError:
        return 'None'