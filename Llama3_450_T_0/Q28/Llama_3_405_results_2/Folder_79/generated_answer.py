def return_nth_smallest_ascii(s):
    chars = sorted(s[13:36])
    return sorted(chars, key=lambda x: ord(x))[17]