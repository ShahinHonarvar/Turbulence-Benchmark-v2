def all_odd_ints_inclusive(nested_list):
    target_list = nested_list[82:87]
    odd_ints = [num for num in target_list if num % 2 != 0]
    return odd_ints