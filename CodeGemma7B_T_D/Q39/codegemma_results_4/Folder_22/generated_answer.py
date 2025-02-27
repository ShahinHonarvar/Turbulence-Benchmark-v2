def return_n_greatest_chars(string):
    """Function that sorts the most recent 76 characters by ASCII values."""
    result = sorted(list(string)[-76:], key=ord)
    return result