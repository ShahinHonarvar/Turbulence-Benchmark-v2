def return_nth_smallest_ascii(string):
    subset = string[14:67]
    sorted_chars = sorted(set(subset))
    if len(sorted_chars) >= 8:
        return sorted_chars[7]
    else:
        return None