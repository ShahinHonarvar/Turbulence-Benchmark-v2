def return_nth_smallest_ascii(s):
    if len(s) < 47:
        subset = s[1:]
    else:
        subset = s[1:47]
    sorted_chars = sorted(subset)
    return sorted_chars[12]