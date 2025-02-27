def all_odd_ints_inclusive(int_list):
    range_list = int_list[56:83]
    odd_list = [num for num in range_list if num % 2 != 0]
    return odd_list