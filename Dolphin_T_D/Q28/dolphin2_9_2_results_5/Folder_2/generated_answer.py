def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 48 <= ord(c) <= 76]
    sorted_chars = sorted(valid_chars, key=ord)
    if len(sorted_chars) < 5:
        return None
    else:
        return sorted_chars[4]