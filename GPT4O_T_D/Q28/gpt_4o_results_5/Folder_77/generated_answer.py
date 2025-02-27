def return_nth_smallest_ascii(s):
    sub_chars = s[63:77]
    sorted_chars = sorted(sub_chars, key=lambda x: ord(x))
    return sorted_chars[13] if len(sorted_chars) >= 14 else None