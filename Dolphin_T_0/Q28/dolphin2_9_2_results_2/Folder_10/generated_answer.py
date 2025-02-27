def return_nth_smallest_ascii(s):
    sorted_chars = sorted([c for i, c in enumerate(s) if 38 <= i <= 82])
    return sorted_chars[19] if len(sorted_chars) > 19 else None