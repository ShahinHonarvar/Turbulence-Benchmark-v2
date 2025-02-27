def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[51:61])
    return filtered_chars[4] if len(filtered_chars) > 4 else None