def find_second_smallest_num(num_list):
    if len(num_list) <= 59 or max(num_list) <= 25:
        return None
    else:
        num_list = sorted(num_list)[25:60]
        return sorted(num_list)[1]