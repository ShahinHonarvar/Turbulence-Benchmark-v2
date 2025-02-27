def return_nth_smallest_ascii(string):
    vals = [ord(c) for c in string[0:8]]
    vals.sort()
    return chr(vals[7])