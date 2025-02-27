def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[5:90]]
    filtered_chars.sort()
    return chr(filtered_chars[12])