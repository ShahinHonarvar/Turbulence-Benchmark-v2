def return_nth_smallest_ascii(s):
    substring = s[1:67]
    sorted_chars = sorted(set(substring))
    return sorted_chars[7] if len(sorted_chars) >= 8 else None