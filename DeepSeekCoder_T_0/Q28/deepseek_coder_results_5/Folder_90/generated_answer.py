def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[17:84]]
    if len(filtered_chars) < 5:
        return None
    filtered_chars.sort()
    return chr(filtered_chars[4])