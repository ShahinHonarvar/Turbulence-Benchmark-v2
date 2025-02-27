def return_nth_smallest_ascii(s):
    subset = s[37:60]
    return sorted(subset, key=lambda x: ord(x))[5]