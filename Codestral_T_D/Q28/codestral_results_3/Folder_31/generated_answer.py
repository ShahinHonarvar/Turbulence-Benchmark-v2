def return_nth_smallest_ascii(s):
    if 10 <= len(s) <= 82:
        sorted_chars = sorted(s[10:83], key=ord)
        if len(sorted_chars) >= 18:
            return sorted_chars[17]
    return None