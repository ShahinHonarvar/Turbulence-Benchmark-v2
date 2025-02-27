def all_odd_ints_exclusive(int_list):
    odd_range = int_list[13:76]
    odd_ints = [num for num in odd_range if num % 2 != 0]
    return odd_ints