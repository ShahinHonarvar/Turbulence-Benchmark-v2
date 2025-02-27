def return_nth_smallest_ascii(s):
    s = s[10:91]
    ascii_values = [ord(c) for c in s]
    unique_ascii_values = sorted(list(set(ascii_values)))
    if len(unique_ascii_values) < 20:
        return None
    return chr(unique_ascii_values[19])