def find_second_smallest_num(num_list):
    if len(num_list) < len(range(34, 56)):
        return 'None'
    num_list_filtered = sorted([num for num in num_list if 34 <= num <= 55])
    return num_list_filtered[1] if len(num_list_filtered) >= 2 else 'None'