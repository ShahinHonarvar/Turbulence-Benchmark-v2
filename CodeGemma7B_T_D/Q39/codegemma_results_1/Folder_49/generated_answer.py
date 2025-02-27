def return_n_greatest_chars(string):
    """Return the n greatest chars in a string sorted in descending order."""
    greatest_chars = sorted(string, key=ord, reverse=True)[:76]
    return greatest_chars