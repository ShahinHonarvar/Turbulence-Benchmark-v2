def return_nth_smallest_ascii(s):
    chars = s[:17]
    return sorted(chars, key=lambda k: ord(k))[16]