def return_nth_smallest_ascii(s):
    vals = [ord(ch) for ch in s[3:53]]
    vals.sort()
    return chr(vals[7])