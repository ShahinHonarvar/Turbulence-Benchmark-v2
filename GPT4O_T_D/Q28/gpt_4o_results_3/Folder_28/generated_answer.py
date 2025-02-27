def return_nth_smallest_ascii(s):
    substring = s[25:78]
    sorted_chars = sorted(substring, key=lambda x: ord(x))
    return sorted_chars[15] if len(sorted_chars) >= 16 else None