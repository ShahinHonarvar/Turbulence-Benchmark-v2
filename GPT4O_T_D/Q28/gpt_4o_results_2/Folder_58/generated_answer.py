def return_nth_smallest_ascii(s):
    sub_str = s[8:27]
    sorted_chars = sorted(sub_str, key=lambda c: ord(c))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None