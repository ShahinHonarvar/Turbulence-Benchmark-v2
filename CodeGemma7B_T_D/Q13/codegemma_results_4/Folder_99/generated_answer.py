def find_second_largest_num(num_list):
    max_element = max(num_list)
    num_list.remove(max_element)
    second_max_element = max(num_list)
    if second_max_element in num_list[310:371]:
        return second_max_element
    else:
        return 'None'