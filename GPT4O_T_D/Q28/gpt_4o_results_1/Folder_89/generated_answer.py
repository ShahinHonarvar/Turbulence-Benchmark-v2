def return_nth_smallest_ascii(s):
    filtered_chars = s[24:72]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[7] if len(sorted_chars) >= 8 else None