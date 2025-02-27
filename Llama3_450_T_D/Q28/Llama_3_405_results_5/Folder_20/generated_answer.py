def return_nth_smallest_ascii(s):
    substring = s[25:65]
    unique_chars = sorted(set(substring))
    return sorted(unique_chars, key=lambda x: ord(x))[5]