def return_nth_smallest_ascii(s):
    substring = s[0:10]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    return sorted_chars[9]