def return_nth_smallest_ascii(s):
    filtered_chars = s[52:80]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None