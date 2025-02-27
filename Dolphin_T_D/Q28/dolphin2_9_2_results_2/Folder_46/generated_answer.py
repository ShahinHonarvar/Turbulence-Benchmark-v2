def return_nth_smallest_ascii(s):
    chars = s[34:86]
    sorted_chars = [c for c in chars]
    sorted_chars.sort(key=lambda c: ord(c))
    if len(sorted_chars) >= 20:
        return sorted_chars[19]
    return None