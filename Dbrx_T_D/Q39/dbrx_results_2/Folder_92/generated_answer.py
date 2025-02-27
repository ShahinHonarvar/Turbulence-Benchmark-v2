def return_n_greatest_chars(string_of_chars):
    sorted_chars = [char for char in sorted(string_of_chars, reverse=True)]
    return sorted_chars[:63] if len(sorted_chars) > 63 else sorted_chars