def all_odd_ints_inclusive(lst):
    new_lst = [num for num in lst[:7] if num % 2 != 0]
    return new_lst if new_lst else []