def find_second_smallest_num(num_list):
    if len(num_list) < 67:
        return None
    else:
        target_list = num_list[56:67]
        target_list.sort()
        if len(target_list) < 2:
            return None
        else:
            return target_list[1]