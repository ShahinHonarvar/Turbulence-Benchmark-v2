def return_nth_smallest_ascii(s):
    filtered_chars = [char for idx, char in enumerate(s) if 63 <= idx <= 76]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None