def return_nth_smallest_ascii(s):
    segment = s[67:78]
    sorted_chars = sorted(segment, key=ord)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None