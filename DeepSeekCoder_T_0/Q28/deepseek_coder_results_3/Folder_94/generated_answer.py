def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[6:59]]
    filtered_chars.sort()
    return chr(filtered_chars[18]) if len(filtered_chars) > 18 else None