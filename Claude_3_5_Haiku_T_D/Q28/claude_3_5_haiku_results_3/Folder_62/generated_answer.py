def return_nth_smallest_ascii(s):
    subset = s[51:79]
    sorted_chars = sorted(set(subset), key=ord)
    return sorted_chars[8]