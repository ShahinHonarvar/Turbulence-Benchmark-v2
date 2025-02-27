def return_nth_smallest_ascii(s):
    chars = [c for c in s[10:74]]
    return sorted(chars, key=ord)[8]