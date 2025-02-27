def return_nth_smallest_ascii(s):
    subrange = s[18:67]
    sorted_chars = sorted(subrange, key=lambda c: ord(c))
    return sorted_chars[18] if len(sorted_chars) >= 19 else None