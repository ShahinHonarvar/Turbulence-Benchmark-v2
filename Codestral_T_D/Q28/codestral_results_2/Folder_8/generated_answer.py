def return_nth_smallest_ascii(s):
    substring = s[60:89]
    unique_chars = list(set(substring))
    unique_chars.sort(key=ord)
    return unique_chars[6] if len(unique_chars) > 6 else None