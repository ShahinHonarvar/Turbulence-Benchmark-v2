def return_nth_smallest_ascii(s):
    chars = s[15:22]
    values = [ord(c) for c in chars]
    return chr(sorted(values)[5])