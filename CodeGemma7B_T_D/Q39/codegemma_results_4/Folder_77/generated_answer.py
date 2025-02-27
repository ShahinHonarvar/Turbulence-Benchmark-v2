from functools import cmp_to_key

def return_n_greatest_chars(s):
    """
    Returns a sorted list of the greatest ASCII values of a string.
    """
    return sorted(s, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)[:47]