def return_nth_smallest_ascii(s):
    chars = sorted(s[:46])
    return sorted(chars, key=lambda x: ord(x))[9]