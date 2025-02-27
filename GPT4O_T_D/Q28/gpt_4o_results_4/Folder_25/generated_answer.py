def return_nth_smallest_ascii(s):
    substring = s[34:69]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None