def return_nth_smallest_ascii(s):
    subset = s[36:80]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 12:
        return sorted_chars[11]
    else:
        return None