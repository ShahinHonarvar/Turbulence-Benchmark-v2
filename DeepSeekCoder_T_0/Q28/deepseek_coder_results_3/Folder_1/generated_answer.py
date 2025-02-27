def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[21:60]]
    filtered_chars.sort()
    return chr(filtered_chars[10]) if len(filtered_chars) > 10 else None