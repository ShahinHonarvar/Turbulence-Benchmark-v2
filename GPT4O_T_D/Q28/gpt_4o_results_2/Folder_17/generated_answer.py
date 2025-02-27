def return_nth_smallest_ascii(s):
    filtered_chars = s[4:34]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None