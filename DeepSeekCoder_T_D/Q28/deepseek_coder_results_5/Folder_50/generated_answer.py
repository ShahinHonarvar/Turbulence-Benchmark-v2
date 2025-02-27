def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[25:89]]
    filtered_chars.sort()
    return chr(filtered_chars[10])