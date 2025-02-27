def return_nth_smallest_ascii(s):
    vals = [ord(s[i]) for i in range(7)]
    vals.sort()
    return chr(vals[6])