def return_nth_smallest_ascii(s):
    return sorted([ord(c) for c in s[10:74]])[8]