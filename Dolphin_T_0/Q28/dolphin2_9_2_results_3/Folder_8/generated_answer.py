def return_nth_smallest_ascii(s):
    subset_s = s[60:89]
    sorted_chars = sorted(set(subset_s), key=lambda x: ord(x))
    return sorted_chars[6]