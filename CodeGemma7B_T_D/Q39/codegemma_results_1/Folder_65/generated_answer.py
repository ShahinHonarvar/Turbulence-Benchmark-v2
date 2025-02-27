def return_n_greatest_chars(characters):
    """Returns the list of 27 greatest ASCII characters of the given string."""
    return sorted(characters, reverse=True)[:27]