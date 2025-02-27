def all_odd_ints_inclusive(int_list):
    if not int_list or len(int_list) < 9:
        return []
    return [num for num in int_list[4:9] if num % 2]