def return_nth_smallest_ascii(s):
    chars = sorted(s[8:27])
    return min(chars, key=lambda c: (ord(c), chars.index(c)))[5]

def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[8:27]])
    return chr(ascii_values[5])