def return_nth_smallest_ascii(s):
    chars = sorted(s[:13])
    return sorted(chars, key=lambda x: ord(x))[12]