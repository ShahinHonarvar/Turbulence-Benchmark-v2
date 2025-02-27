def return_n_smallest_chars(chars):
    """sorts a list of distinct characters by their ASCII values and returns the first 46 characters."""
    return sorted([c for c in sorted(chars)])[:46]