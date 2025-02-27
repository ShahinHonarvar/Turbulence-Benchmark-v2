def return_nth_smallest_ascii(s):
    subset = s[5:83]
    sorted_chars = sorted(list(set(subset)), key=lambda c: ord(c))
    return sorted_chars[15]