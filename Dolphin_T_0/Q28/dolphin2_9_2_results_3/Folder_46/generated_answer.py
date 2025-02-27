def return_nth_smallest_ascii(s):
    values = [ord(c) for c in s[34:86]]
    values.sort()
    return chr(values[19])