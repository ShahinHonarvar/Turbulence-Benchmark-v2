def return_n_greatest_chars(text):
    """Returns a sorted list of the greatest 64 characters"""
    return ''.join(sorted(text, key=ord, reverse=True)[:64])