def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[33:86] if char in s]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[12] if len(sorted_chars) > 12 else None