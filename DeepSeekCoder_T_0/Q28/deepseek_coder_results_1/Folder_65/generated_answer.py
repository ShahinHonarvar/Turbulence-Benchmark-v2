def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[32:68]]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[11] if len(sorted_chars) > 11 else None