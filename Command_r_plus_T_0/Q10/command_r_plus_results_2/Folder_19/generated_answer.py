def all_odd_ints_exclusive(int_list):
    odd_range = int_list[2:5]
    return [num for num in odd_range if num % 2 != 0]