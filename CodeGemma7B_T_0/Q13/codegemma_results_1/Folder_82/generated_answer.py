def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 21:
        return 'None'
    num_list = sorted(num_list[20:201], reverse=True)
    if num_list[1] == num_list[0]:
        return 'None'
    return num_list[1]