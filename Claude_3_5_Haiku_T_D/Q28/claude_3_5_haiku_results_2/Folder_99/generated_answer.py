def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[17:66]]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[7] if len(sorted_chars) >= 8 else None