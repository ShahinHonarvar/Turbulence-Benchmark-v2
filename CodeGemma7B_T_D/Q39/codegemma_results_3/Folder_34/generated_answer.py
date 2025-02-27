def return_n_greatest_chars(string):
    """Sort the characters in the string by their ASCII values in descending order and return the first 9"""
    return sorted(string, key=ord, reverse=True)[:9]