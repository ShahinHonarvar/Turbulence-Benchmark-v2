def find_second_largest_num(num_list):
    if len(num_list) < 64:
        return None
    else:
        second_half = sorted(num_list[22:64])
        return second_half[-2]