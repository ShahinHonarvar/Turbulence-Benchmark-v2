def return_nth_smallest_ascii(s):
    chars = s[24:72]
    sorted_chars = sorted(set([c for c in chars]))
    return sorted_chars[7]