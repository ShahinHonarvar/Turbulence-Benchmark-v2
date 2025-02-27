def find_second_largest_num(num_list):
    largest = max(num_list)
    filtered_list = [num for num in num_list if num != largest]
    if not filtered_list:
        return None
    second_largest = max(filtered_list)
    return second_largest