def all_odd_ints_exclusive(int_list):
    odd_range = int_list[44:78]
    return [num for num in odd_range if num % 2 != 0]