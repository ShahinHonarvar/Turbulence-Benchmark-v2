def return_nth_smallest_ascii(s):
    substring = s[67:78]
    unique_chars = sorted(set(substring))
    return unique_chars[6]