def find_second_largest_num(num_list):
    try:
        target_list = sorted(num_list[50:55], reverse=True)
        return target_list[1]
    except IndexError:
        return None