def return_nth_smallest_ascii(s):
    substring = s[5:11]
    sorted_chars = sorted(substring)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None