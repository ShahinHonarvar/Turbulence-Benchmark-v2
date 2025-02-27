def all_odd_ints_inclusive(lst):
    selected_ints = [num for num in lst[30:49] if num % 2 != 0]
    return selected_ints if selected_ints else []