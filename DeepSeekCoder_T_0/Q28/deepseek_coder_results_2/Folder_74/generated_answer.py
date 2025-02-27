def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[1:32]]
    filtered_chars.sort()
    return chr(filtered_chars[5]) if len(filtered_chars) > 5 else None