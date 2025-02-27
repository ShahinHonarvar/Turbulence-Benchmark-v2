def return_nth_smallest_ascii(s):
    substring = sorted(s[47:81])
    return substring[3] if len(substring) > 3 else None