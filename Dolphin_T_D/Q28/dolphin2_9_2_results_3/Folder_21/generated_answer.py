def return_nth_smallest_ascii(s):
    chars = [c for c in s[8:66] if ord(c) not in [10, 13]]
    return sorted(chars, key=ord)[5]