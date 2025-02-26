def return_nth_smallest_ascii(s):
    subset = s[10:83]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 18:
        return sorted_chars[17]
    else:
        return None