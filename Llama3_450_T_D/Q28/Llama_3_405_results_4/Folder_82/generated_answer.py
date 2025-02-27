def return_nth_smallest_ascii(s):
    chars = sorted(s[:15])
    return min(chars, key=lambda x: (ord(x) >= ord(sorted(set(chars))[14]), -ord(x)))