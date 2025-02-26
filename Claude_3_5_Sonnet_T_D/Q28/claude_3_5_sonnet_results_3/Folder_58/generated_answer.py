def return_nth_smallest_ascii(string):
    subset = string[8:27]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    else:
        return None