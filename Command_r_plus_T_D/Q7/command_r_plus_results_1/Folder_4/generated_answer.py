def all_even_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 12 and i <= 92 and (num % 2 == 0)]