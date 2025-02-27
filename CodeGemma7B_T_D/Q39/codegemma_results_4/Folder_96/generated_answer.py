def return_n_greatest_chars(chars):
    """return the largest n characters in the string"""
    greatest_chars = sorted(chars, key=ord, reverse=True)[:20]
    return greatest_chars[::20]