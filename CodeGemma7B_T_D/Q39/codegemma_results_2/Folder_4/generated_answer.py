def return_n_greatest_chars(string):
    """Returns the sorted list of the 90 greatest ASCII characters of the given string."""
    return sorted(string, key=ord, reverse=True)[:90]