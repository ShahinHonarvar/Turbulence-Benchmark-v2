def all_odd_ints_inclusive(int_list):
    return [num for num in int_list if num % 2 != 0 and num in range(0, 8)]