def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(47, 81)]
    asc = [ord(c) for c in chars]
    asc.sort()
    return chars[asc.index(asc[3])]