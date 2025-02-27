def return_nth_smallest_ascii(s):
    chars = s[25:65]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[5]