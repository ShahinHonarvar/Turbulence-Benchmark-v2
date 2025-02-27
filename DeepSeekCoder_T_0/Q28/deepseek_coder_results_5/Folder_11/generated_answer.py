def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[9:60]]
    if len(filtered_chars) < 6:
        return None
    filtered_chars.sort()
    return chr(filtered_chars[5])