def return_nth_smallest_ascii(s):
    sorted_chars = sorted([c for c in s[36:80] if c.isalpha()])
    if len(sorted_chars) >= 12:
        return sorted_chars[11]
    else:
        return None