def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[51:90]]
    filtered_chars.sort()
    return chr(filtered_chars[13])