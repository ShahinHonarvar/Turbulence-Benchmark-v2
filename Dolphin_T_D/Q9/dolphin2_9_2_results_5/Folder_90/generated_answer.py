def all_odd_ints_inclusive(input_list):
    return [x for i, x in enumerate(input_list) if i in range(262, 747) and x % 2 == 1]