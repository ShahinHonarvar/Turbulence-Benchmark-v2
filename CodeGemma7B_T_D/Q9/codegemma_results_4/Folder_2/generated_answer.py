def all_odd_ints_inclusive(int_list):
    """Return odd numbers in range(15, 39, 2)."""
    return [num for num in int_list[15:39 + 1] if num % 2 != 0]