def return_n_greatest_chars(text):
    """Return the N greatest characters in a string"""
    return sorted([char for char in text], reverse=True)[:37]