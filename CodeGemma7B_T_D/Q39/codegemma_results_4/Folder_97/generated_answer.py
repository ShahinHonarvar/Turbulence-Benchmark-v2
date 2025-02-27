def return_n_greatest_chars(text):
    """Return the sorted list of the 38 greatest characters in a string."""
    return sorted(text, key=ord)[-38:]