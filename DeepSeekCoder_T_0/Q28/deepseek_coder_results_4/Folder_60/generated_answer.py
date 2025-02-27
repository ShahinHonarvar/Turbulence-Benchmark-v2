def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[36:80]]
    filtered_chars.sort()
    return filtered_chars[11] if len(filtered_chars) > 11 else None