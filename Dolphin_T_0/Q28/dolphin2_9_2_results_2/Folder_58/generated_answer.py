def return_nth_smallest_ascii(s):
    subset = s[8:27]
    sorted_chars = sorted(subset, key=lambda c: ord(c))
    return sorted_chars[5]