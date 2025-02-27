def all_even_ints_inclusive(int_list):
    """Returns a list of all even integers from index 50 to index 54, inclusive."""
    return [i for i in range(50, 55) if i in int_list and i % 2 == 0]