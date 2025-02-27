def all_odd_ints_inclusive(input_list):
    result = [x for i, x in enumerate(input_list) if 10 <= i <= 66 and x % 2 != 0]
    return result