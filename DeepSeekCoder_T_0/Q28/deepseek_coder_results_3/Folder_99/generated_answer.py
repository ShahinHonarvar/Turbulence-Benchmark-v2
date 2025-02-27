def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[17:66]]
    filtered_chars.sort()
    return chr(filtered_chars[7])