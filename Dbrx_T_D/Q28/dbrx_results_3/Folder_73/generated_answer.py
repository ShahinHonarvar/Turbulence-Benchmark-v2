def return_nth_smallest_ascii(s):
    sorted_chars = sorted(set(s[:70]))
    if len(sorted_chars) < 10:
        return sorted_chars[-1]
    else:
        return sorted_chars[9]