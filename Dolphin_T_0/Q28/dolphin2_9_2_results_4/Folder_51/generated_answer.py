def return_nth_smallest_ascii(s):
    values = [ord(c) for c in s[10:74]]
    values.sort()
    return chr(values[9])