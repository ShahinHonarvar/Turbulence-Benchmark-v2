def return_nth_smallest_ascii(string):
    subset = string[14:55]
    sorted_chars = sorted(subset)
    return sorted_chars[10] if len(sorted_chars) > 10 else None