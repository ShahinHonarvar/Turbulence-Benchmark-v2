def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 48 <= ord(c) <= 76]
    valid_chars.sort(key=ord)
    if len(valid_chars) >= 5:
        return valid_chars[4]
    else:
        return None