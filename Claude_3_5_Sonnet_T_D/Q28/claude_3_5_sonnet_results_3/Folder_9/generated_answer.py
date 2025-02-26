def return_nth_smallest_ascii(string):
    subset = string[10:91]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 20:
        return sorted_chars[19]
    else:
        return None