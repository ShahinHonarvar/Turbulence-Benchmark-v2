def return_nth_smallest_ascii(s):
    filtered_chars = [ord(c) for c in s[38:65]]
    filtered_chars.sort()
    return chr(filtered_chars[13])