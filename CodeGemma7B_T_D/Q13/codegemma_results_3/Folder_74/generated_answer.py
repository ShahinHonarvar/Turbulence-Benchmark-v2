def find_second_largest_num(num_list):
    num_list = num_list[17:79]
    num_list.sort(reverse=True)
    return num_list[1] if len(num_list) >= 2 else 'None'