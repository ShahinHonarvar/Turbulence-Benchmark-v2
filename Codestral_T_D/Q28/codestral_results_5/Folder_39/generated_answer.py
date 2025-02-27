def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[1:67], key=ord)
    return sorted_chars[7] if len(sorted_chars) > 7 else None