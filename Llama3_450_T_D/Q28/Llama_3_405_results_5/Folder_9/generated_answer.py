def return_nth_smallest_ascii(s):
    substring = s[10:91]
    ascii_sorted = sorted(substring, key=lambda c: ord(c))
    return ascii_sorted[19]