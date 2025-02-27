def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 33 <= ord(c) <= 60]
    valid_chars.sort(key=ord)
    return valid_chars[17] if len(valid_chars) > 17 else None