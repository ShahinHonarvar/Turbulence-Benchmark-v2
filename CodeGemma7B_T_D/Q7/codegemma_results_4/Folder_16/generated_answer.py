def all_even_ints_inclusive(number_list):
    new_list = number_list[:33]
    filtered_list = [num for num in new_list[33:37] if num % 2 == 0]
    return filtered_list if filtered_list else []