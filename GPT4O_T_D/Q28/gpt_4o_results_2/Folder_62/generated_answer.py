def return_nth_smallest_ascii(s):
    sub_chars = s[51:79]
    sorted_chars = sorted(sub_chars)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None