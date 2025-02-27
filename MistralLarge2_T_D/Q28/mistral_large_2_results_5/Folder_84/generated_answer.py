def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[52:80])
    return sorted_chars[6] if len(sorted_chars) >= 7 else None