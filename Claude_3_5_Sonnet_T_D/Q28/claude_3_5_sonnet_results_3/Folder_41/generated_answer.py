def return_nth_smallest_ascii(string):
    subset = string[58:86]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    else:
        return None