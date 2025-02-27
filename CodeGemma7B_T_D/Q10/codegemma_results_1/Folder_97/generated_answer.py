def all_odd_ints_exclusive(int_list):
    filtered_list = [num for num in int_list if num % 2 != 0 and 20 < num < 93]
    return filtered_list if filtered_list else []