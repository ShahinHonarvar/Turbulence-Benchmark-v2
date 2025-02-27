def return_nth_smallest_ascii(s):
    chars = [c for c in s[33:86] if 33 <= ord(c) <= 85]
    return sorted(chars, key=ord)[12]