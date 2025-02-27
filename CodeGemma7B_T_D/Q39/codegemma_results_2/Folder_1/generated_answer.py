def return_n_greatest_chars(a):
    """
    returns the sorted list of exactly 11 characters
    of the given string a
    that have the greatest ASCII values
    """
    new = ''.join(sorted(a, reverse=True))[:11]
    return new