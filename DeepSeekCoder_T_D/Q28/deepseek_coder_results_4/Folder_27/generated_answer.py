def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[33:86] if char.isalpha()]
    filtered_chars.sort()
    return filtered_chars[12] if len(filtered_chars) > 12 else None