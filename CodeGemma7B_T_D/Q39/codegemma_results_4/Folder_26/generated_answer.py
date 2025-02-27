def return_n_greatest_chars(string):
    """Sort characters by ASCII values in ascending order. Return a sorted list of the greatest 43 characters."""
    return sorted(string, key=ord)[-43:]