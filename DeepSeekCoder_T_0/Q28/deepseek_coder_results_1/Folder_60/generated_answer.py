def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[36:80]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[11] if len(sorted_chars) > 11 else None