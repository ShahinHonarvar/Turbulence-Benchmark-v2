def return_nth_smallest_ascii(s):
    substring = s[18:46]
    sorted_chars = sorted(substring)
    return sorted_chars[6] if len(sorted_chars) > 6 else None