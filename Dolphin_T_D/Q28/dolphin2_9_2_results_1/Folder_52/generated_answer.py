def return_nth_smallest_ascii(s):
    chars = [c for c in s[46:73]]
    return sorted(chars, key=lambda x: ord(x))[14]