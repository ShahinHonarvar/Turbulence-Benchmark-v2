def return_nth_smallest_ascii(s):
    substring = s[44:70]
    ascii_sorted_chars = sorted(substring, key=lambda x: ord(x))
    return ascii_sorted_chars[14]