from functools import cmp_to_key

def return_n_greatest_chars(text):
    """
    sorts and returns the 24 characters of a string which have highest ASCII Values
    """
    return sorted(text, key=cmp_to_key(lambda a, b: ord(a) - ord(b)), reverse=False)[:24]