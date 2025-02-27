def find_second_largest_num(num_lst):
    filtered_lst = [num for num in num_lst[40:201] if num < max(num_lst)]
    return filtered_lst[-2] if filtered_lst else 'None'