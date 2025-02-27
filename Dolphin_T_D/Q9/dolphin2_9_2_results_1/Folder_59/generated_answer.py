def all_odd_ints_inclusive(num_list):
    return [num for i, num in enumerate(num_list) if i >= 0 and i <= 9 and (num % 2 != 0)]