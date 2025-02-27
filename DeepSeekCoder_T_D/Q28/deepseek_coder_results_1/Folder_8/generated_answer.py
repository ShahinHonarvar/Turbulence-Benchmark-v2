def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[60:89]]
    if len(filtered_chars) < 7:
        return None
    filtered_chars.sort()
    return filtered_chars[6]