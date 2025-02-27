def return_nth_smallest_ascii(s):
    subset = s[46:73]
    sorted_chars = sorted(set(subset), key=lambda x: ord(x))
    return sorted_chars[14]