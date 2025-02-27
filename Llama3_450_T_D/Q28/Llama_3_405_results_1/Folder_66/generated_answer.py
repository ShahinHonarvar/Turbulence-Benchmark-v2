def return_nth_smallest_ascii(s):
    substring = s[35:53]
    unique_chars = sorted(set(substring))
    return unique_chars[9]