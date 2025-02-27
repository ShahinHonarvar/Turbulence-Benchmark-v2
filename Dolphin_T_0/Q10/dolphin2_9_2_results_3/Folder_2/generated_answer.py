def all_odd_ints_exclusive(lst):
    odd_integers = [num for i, num in enumerate(lst[37:53]) if num % 2 != 0]
    return odd_integers