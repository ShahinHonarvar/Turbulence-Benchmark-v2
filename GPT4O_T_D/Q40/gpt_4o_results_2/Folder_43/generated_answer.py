def return_n_smallest_chars(char_string):
    if len(char_string) < 56:
        return sorted(char_string, reverse=True)
    smallest_chars = sorted(char_string)[:56]
    return sorted(smallest_chars, reverse=True)