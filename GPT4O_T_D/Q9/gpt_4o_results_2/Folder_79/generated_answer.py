def all_odd_ints_inclusive(int_list):
    if len(int_list) < 5:
        return []
    return [num for num in int_list[4:5] if num % 2 != 0]