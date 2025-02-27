def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[58:86]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[18] if len(sorted_chars) > 18 else None