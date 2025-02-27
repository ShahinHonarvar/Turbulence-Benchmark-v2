def all_odd_ints_inclusive(int_list):
    filtered_list = [num for num in int_list[661:925] if num % 2 != 0]
    return filtered_list if filtered_list else []