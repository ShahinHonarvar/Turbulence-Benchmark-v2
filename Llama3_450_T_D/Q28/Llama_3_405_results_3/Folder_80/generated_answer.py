def return_nth_smallest_ascii(s):
    substring = s[51:90]
    sorted_chars = sorted(substring)
    return sorted(sorted_chars, key=lambda x: ord(x))[13]