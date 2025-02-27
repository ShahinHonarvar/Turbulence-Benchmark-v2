def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[38:65]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[13] if len(sorted_chars) > 13 else None