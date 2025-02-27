def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(47, 71)]
    asciis = [ord(c) for c in chars]
    asciis.sort()
    return chars[asciis.index(asciis[13])]