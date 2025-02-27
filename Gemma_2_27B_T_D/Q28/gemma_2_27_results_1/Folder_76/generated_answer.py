def return_nth_smallest_ascii(s):
    subset = sorted([ord(char) for char in s[18:67]])
    return chr(subset[18])