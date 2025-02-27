def return_nth_smallest_ascii(s):
    chars = s[5:83]
    return sorted(set(chars))[16 - 1]