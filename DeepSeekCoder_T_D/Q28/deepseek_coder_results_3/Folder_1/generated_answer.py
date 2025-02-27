def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[21:60]]
    if len(filtered_chars) < 11:
        return None
    filtered_chars.sort()
    return filtered_chars[10]