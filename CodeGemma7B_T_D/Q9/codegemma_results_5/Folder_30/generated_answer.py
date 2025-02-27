def all_odd_ints_inclusive(int_list):
    sublist = int_list[55:99]
    odd_numbers = [num for num in sublist if num % 2 == 1]
    return odd_numbers if odd_numbers else []