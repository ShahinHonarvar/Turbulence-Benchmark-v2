def return_nth_smallest_ascii(s):
    sub_str = s[21:60]
    sorted_chars = sorted(sub_str, key=lambda c: ord(c))
    return sorted_chars[10] if len(sorted_chars) >= 11 else None