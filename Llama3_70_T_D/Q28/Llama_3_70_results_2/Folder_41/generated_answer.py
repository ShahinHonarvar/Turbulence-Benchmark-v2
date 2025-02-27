def return_nth_smallest_ascii(s):
    chars = sorted([s[i] for i in range(58, 86)])
    asciis = sorted(list(set([ord(c) for c in chars])))
    return chr(asciis[18])