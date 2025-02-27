def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 34 <= i <= 85]
    if len(filtered_chars) < 20:
        return None
    filtered_chars.sort()
    return filtered_chars[19]