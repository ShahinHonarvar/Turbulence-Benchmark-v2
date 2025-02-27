def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s if 34 <= s.index(c) <= 68]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[5] if len(sorted_chars) > 5 else None