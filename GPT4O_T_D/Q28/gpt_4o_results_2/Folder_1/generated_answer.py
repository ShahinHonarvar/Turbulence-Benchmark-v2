def return_nth_smallest_ascii(s):
    sub_chars = s[21:60]
    sorted_chars = sorted(sub_chars, key=lambda x: ord(x))
    return sorted_chars[10] if len(sorted_chars) >= 11 else None