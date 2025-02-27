def return_nth_smallest_ascii(s):
    chars = sorted(s[30:71])
    asc = [ord(c) for c in chars]
    asc.sort()
    return chr(asc[14])