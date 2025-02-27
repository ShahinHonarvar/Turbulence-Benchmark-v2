def find_second_smallest_num(list_of_numbers):
    sorted_list = sorted(list_of_numbers)[62:65]
    if len(sorted_list) > 1:
        return sorted_list[1]
    else:
        return 'None'