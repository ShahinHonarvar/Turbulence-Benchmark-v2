def return_nth_smallest_ascii(s):
    values = [ord(c) for c in s[60:84] if s.index(c) >= 60 and s.index(c) <= 83]
    values.sort()
    return chr(values[13])