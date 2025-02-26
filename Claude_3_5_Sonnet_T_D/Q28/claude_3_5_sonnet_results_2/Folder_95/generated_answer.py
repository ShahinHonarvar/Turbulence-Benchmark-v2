def return_nth_smallest_ascii(s):
    substring = s[1:47]
    sorted_chars = sorted(set(substring), key=ord)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None