def find_second_largest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list) <= 22 or len(num_list) > 90:
        return None
    else:
        return num_list[-2]