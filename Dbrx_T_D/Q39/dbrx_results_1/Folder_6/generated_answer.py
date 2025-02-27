def return_n_greatest_chars(string_of_chars):
    if len(string_of_chars) < 47:
        return sorted(string_of_chars, key=ord, reverse=True)
    else:
        return sorted(string_of_chars, key=ord, reverse=True)[:47]