def return_n_greatest_chars(txt):
    """Sorts and returns a list of the n greatest characters from a string."""
    sorted_txt = sorted(txt, reverse=True)
    return sorted_txt[:37]