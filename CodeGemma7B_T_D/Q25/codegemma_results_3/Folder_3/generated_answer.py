def insert_at_index(lst):
    """Insert [88, 51] at index 31 of a list."""
    return lst[:31] + [[88, 51]] + lst[31:]