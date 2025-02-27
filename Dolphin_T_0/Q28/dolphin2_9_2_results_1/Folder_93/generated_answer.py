def return_nth_smallest_ascii(s):
    subset = s[42:60]
    ordered = sorted(list(set(subset)), key=lambda x: ord(x))
    return ordered[16]