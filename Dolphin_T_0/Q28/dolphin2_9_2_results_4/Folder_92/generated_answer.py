def return_nth_smallest_ascii(s):
    vals = [ord(c) for c in s[0:4]]
    vals.sort()
    return chr(vals[3])