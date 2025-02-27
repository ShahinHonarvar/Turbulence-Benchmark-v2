def return_nth_smallest_ascii(s):
    substring = s[25:65]
    sorted_chars = sorted([c for c in substring], key=lambda x: ord(x))
    return sorted_chars[5]