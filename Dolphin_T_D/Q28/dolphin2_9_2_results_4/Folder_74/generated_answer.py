def return_nth_smallest_ascii(s):
    vals = [ord(c) for c in s[1:32]]
    return chr(sorted(vals)[5])