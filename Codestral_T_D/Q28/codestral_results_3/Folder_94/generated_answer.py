def return_nth_smallest_ascii(s):
    substring = s[6:59]
    unique_chars = list(set(substring))
    unique_chars.sort(key=ord)
    return unique_chars[18]