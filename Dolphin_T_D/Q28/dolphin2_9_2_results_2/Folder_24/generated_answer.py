def return_nth_smallest_ascii(s):
    substring = s[34:82]
    sorted_chars = sorted(substring, key=lambda x: (ord(x), substring.index(x)), reverse=True)
    return sorted_chars[11]