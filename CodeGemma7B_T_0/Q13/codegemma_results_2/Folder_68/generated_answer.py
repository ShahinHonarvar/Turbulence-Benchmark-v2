def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2:
        return 'None'
    largest = max(num_list[:9])
    num_list.remove(largest)
    return max(num_list[:9])