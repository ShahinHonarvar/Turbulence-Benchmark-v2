def return_nth_smallest_ascii(s):
    substring = s[29:48]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[6]