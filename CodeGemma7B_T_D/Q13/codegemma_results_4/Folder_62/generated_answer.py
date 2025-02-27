def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 100:
        return None
    num_list.sort(reverse=True)
    if 91 <= len(num_list) <= 99:
        return num_list[91]
    else:
        return None