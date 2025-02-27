def return_nth_smallest_ascii(s):
    sub = s[51:79]
    values = [ord(c) for c in sub]
    values.sort()
    return chr(values[8])