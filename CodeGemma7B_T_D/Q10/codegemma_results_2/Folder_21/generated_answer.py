def all_odd_ints_exclusive(num_list):
    filtered_list = [num for num in num_list[743:867] if num % 2 == 1]
    return filtered_list or []