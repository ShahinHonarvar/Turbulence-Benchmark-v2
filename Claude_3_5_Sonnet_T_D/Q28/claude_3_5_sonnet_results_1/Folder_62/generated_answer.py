def return_nth_smallest_ascii(s):
    subset = s[51:79]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 9:
        return sorted_chars[8]
    else:
        return None