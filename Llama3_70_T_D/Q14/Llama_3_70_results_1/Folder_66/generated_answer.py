def find_second_smallest_num(num_list):
    if 62 <= len(num_list) <= 99:
        return sorted(num_list[62:100])[1]
    else:
        return None