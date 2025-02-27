def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[47:81], key=ord)
    return sorted_chars[3] if len(sorted_chars) > 3 else None