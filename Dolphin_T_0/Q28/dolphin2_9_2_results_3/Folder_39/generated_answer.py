def return_nth_smallest_ascii(s):
    values = [ord(c) for c in s[1:67]]
    values.sort()
    return chr(values[7])