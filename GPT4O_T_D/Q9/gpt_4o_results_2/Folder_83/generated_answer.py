def all_odd_ints_inclusive(int_list):
    if len(int_list) < 91:
        return []
    return [num for num in int_list[90:201] if num % 2 != 0]