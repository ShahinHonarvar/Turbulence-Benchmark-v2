def return_nth_smallest_ascii(s):
    s = s[1:47]
    ascii_values = [ord(c) for c in s]
    unique_ascii_values = sorted(set(ascii_values))
    if len(unique_ascii_values) < 13:
        return None
    else:
        nth_smallest_ascii = unique_ascii_values[12]
        return chr(nth_smallest_ascii)