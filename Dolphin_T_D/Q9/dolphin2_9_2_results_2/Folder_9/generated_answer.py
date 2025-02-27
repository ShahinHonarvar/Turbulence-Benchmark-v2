def all_odd_ints_inclusive(int_list):
    return [int for i, int in enumerate(int_list) if 70 <= i <= 200 and int % 2 != 0]