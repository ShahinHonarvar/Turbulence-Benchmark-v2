def all_even_ints_exclusive(input_list):
    return [num for i, num in enumerate(input_list) if i >= 598 and i < 767 and (num % 2 == 0)]