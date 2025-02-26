def return_nth_smallest_ascii(s):
    substring = s[22:75]
    sorted_chars = sorted(substring)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None