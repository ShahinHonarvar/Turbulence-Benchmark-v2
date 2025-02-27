def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(string_of_chars, key=ord)
    trimmed_chars = sorted_chars[-29:]
    return trimmed_chars