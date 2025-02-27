def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(string_of_chars, key=ord)
    if len(sorted_chars) < 46:
        return sorted_chars
    else:
        return sorted_chars[:46]