def return_nth_smallest_ascii(s):
    sub_str = s[17:84]
    sorted_chars = sorted(sub_str, key=lambda c: ord(c))
    return sorted_chars[4] if len(sorted_chars) >= 5 else None