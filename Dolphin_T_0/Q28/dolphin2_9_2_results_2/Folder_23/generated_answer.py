def return_nth_smallest_ascii(s):
    v = [ord(c) for c in s if 29 <= s.index(c) <= 47]
    return chr(sorted(v)[6])