def return_n_greatest_chars(characters):
    """Returns the sorted list of exactly 24 characters of the given string that have the greatest ASCII values."""
    char_ascii_tuples = [(c, ord(c)) for c in characters]
    char_ascii_tuples.sort(key=lambda x: x[1], reverse=True)
    return [t[0] for t in char_ascii_tuples[:24]]