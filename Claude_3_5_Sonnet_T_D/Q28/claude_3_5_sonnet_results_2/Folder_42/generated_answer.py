def return_nth_smallest_ascii(string):
    subset = string[12:73]
    sorted_chars = sorted(subset)
    return sorted_chars[12] if len(sorted_chars) > 12 else None