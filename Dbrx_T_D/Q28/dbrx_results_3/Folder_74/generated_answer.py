def return_nth_smallest_ascii(s):
    ascii_subset = [ord(c) for c in s if 1 <= s.index(c) <= 31]
    ascii_subset.sort()
    return chr(ascii_subset[6])