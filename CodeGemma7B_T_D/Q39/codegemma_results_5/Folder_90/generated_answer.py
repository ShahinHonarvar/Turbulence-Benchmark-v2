from functools import cmp_to_key

def return_n_greatest_chars(chars):
    """
    Sorts a list of characters by their ASCII values in descending order and returns the first 24 characters.
    """
    return sorted(chars, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=True)[:24]