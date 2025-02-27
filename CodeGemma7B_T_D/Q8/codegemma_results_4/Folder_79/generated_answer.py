def all_even_ints_exclusive(num_list):
    filtered_list = [num for num in num_list[3:8] if num % 2 == 0]
    return filtered_list if filtered_list else []