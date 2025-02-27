def return_nth_smallest_ascii(s):
    relevant_chars = s[34:82]
    ascii_values = sorted([ord(c) for c in relevant_chars])
    return chr(ascii_values[11])