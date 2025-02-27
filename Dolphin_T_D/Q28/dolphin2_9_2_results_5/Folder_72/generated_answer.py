def return_nth_smallest_ascii(s):
    chars = [c for c in s if 33 <= s.index(c) <= 60]
    return sorted(chars, key=lambda x: ord(x))[17]