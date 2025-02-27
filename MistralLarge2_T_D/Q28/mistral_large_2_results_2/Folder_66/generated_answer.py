def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[35:53]))
    return unique_chars[9] if len(unique_chars) >= 10 else None