def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 50 <= i <= 76]
    if len(filtered_chars) < 11:
        return None
    filtered_chars.sort()
    return filtered_chars[10]