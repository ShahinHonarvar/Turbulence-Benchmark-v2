def all_odd_ints_exclusive(int_list):
    odd_integers = [num for i, num in enumerate(int_list[13:66]) if num % 2 != 0]
    return odd_integers