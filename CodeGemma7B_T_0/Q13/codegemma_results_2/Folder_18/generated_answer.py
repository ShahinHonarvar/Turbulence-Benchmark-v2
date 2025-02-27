def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 35 or len(num_list) > 50:
        return None
    num_list = num_list[35:50]
    num_list.sort(reverse=True)
    return num_list[1] if len(num_list) > 1 else None