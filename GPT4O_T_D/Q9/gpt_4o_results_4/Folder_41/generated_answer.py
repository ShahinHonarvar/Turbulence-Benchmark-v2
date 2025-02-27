def all_odd_ints_inclusive(int_list):
    if len(int_list) <= 6:
        return []
    sublist = int_list[6:7]
    return [num for num in sublist if num % 2 != 0]