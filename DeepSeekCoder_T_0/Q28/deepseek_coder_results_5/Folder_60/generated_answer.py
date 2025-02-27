def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 36 <= i <= 79]
    if len(filtered_chars) < 12:
        return None
    filtered_chars.sort()
    return filtered_chars[11]