def return_nth_smallest_ascii(s):
    subset = s[18:67]
    sorted_chars = sorted(subset, key=lambda c: ord(c))
    return sorted_chars[18] if len(sorted_chars) >= 19 else None