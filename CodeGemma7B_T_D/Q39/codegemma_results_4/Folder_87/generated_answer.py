def return_n_greatest_chars(string):
    """The function returns a list of the n greatest characters of the given string based on their ASCII values."""
    n = 24
    char_ascii_values = [(c, ord(c)) for c in string]
    char_ascii_values.sort(key=lambda x: x[1], reverse=True)
    return [c for c, _ in char_ascii_values[:n]]