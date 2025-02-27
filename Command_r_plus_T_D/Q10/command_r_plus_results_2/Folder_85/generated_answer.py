def all_odd_ints_exclusive(int_list):
    odd_range = int_list[4:6]
    return [num for num in odd_range if num % 2 != 0]