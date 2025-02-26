def return_nth_smallest_ascii(string):
    subset = string[51:90]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    else:
        return None