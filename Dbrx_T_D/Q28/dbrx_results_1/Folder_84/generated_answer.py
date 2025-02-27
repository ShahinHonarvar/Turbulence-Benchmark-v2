def return_nth_smallest_ascii(s):
    subset = [ord(c) for c in s if 52 <= s.index(c) <= 79]
    subset.sort()
    return chr(subset[6])