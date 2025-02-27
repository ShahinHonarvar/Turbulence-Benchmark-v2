def return_n_greatest_chars(string):
    """Returns a sorted list of the greatest 26 characters in the given string."""
    return sorted(list(string), key=ord, reverse=True)[:26]