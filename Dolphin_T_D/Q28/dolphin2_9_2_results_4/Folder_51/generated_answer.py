def return_nth_smallest_ascii(s):
    vals = [ord(c) for c in s[10:74]]
    vals.sort()
    return chr(vals[9])