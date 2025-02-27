def all_odd_ints_exclusive(lst):
    odd_numbers = [num for num in lst[1:-1] if num % 2 != 0]
    return odd_numbers