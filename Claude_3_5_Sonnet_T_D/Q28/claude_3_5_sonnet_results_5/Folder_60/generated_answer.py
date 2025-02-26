def return_nth_smallest_ascii(string):
    subset = string[36:80]
    sorted_chars = sorted(subset)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None