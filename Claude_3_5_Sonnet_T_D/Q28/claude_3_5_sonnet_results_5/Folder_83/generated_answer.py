def return_nth_smallest_ascii(string):
    subset = string[30:71]
    sorted_chars = sorted(set(subset))
    if len(sorted_chars) >= 15:
        return sorted_chars[14]
    return None