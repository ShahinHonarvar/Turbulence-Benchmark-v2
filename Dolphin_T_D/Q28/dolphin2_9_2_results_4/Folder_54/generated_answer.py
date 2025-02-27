def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 12 <= s.index(c) <= 87]
    valid_chars.sort(key=lambda c: ord(c))
    if len(valid_chars) >= 17:
        return valid_chars[16]
    else:
        return None