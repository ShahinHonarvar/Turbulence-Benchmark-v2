def return_nth_smallest_ascii(s):
    substring = s[37:60]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    return sorted_chars[5]