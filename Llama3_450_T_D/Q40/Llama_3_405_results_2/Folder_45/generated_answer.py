def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    smallest_chars = []
    for char in unique_chars:
        ascii_val = ord(char)
        if len(smallest_chars) < 52:
            smallest_chars.append(char)
        else:
            break
    return sorted(smallest_chars)