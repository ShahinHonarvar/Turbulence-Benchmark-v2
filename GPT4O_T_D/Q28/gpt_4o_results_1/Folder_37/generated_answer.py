def return_nth_smallest_ascii(s):
    substring = sorted(s[28:68])
    if len(substring) < 15:
        return None
    return substring[14]