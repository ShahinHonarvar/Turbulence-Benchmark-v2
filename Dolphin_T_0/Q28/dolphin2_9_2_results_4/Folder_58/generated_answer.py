def return_nth_smallest_ascii(s):
    chars = [c for c in s[8:27]]
    return sorted(chars, key=ord)[5]