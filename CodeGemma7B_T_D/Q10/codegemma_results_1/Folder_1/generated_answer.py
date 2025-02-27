def all_odd_ints_exclusive(int_list):
    odd_ints = [num for num in range(66, 90) if num % 2 != 0 and num in int_list]
    return odd_ints if odd_ints else []