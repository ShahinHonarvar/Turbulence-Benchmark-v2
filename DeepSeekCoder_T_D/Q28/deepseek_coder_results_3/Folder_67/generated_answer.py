def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 60 <= i <= 83]
    if len(filtered_chars) < 14:
        return None
    filtered_chars.sort()
    return filtered_chars[13]