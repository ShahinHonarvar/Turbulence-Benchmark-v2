def find_second_largest_num(num_list):
    length_of_list = len(num_list)
    if length_of_list < 100:
        return 'None'
    num_list_sorted = sorted(num_list[91:99], reverse=True)
    if num_list_sorted[0] == num_list_sorted[1]:
        return 'None'
    return num_list_sorted[1]