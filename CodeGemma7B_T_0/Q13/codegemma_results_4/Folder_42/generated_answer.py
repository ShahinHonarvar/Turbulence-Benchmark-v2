def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 30 or len(num_list) > 80:
        return 'None'
    num_list.sort(reverse=True)
    return num_list[29] if num_list[29] != num_list[0] else 'None'