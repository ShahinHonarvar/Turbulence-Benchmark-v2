def return_nth_smallest_ascii(s):
    if len(s) < 84:
        return None
    substring = s[17:84]
    ascii_values = sorted(substring)
    return ascii_values[4]