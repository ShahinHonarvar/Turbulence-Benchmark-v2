def return_nth_smallest_ascii(s):
    subset = s[20:81]
    sorted_chars = sorted(subset)
    return sorted_chars[10] if len(sorted_chars) >= 11 else None