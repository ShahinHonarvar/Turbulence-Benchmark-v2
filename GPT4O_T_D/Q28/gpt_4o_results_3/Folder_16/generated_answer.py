def return_nth_smallest_ascii(s):
    sub_str = s[18:46]
    sorted_chars = sorted(sub_str, key=lambda c: ord(c))
    return sorted_chars[6] if len(sorted_chars) >= 7 else None