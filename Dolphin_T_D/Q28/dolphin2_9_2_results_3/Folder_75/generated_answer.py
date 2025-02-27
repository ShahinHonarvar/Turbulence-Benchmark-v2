def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[62:84]]
    return chr(sorted(ascii_values)[8])