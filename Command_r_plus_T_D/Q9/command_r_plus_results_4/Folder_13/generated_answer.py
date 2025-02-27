def all_odd_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 25 and i <= 87 and (num % 2 != 0)]