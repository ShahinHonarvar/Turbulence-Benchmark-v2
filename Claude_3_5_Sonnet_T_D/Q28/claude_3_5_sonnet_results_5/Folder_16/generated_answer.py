def return_nth_smallest_ascii(string):
    subset = string[18:46]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 7:
        return sorted_chars[6]
    else:
        return None