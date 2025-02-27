def find_second_largest_num(num_list):
    if len(num_list) < 67 or max(num_list) < max(num_list)[56:67]:
        return 'None'
    return sorted(num_list)[56:67][-2]