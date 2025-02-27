def return_nth_smallest_ascii(s):
    chars = s[17:66]
    asciis = [ord(c) for c in chars]
    asciis.sort()
    return chars[asciis.index(asciis[7])]