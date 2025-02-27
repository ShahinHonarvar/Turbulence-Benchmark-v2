def find_largest_num(num_list):
    if len(num_list) < 100:
        return 'The list length is less than 100.'
    else:
        return max(num_list[62:100])