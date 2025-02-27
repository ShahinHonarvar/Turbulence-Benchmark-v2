def return_nth_smallest_ascii(s):
    if len(s) < 53:
        return None
    substring = s[35:53]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    return sorted_chars[9] if len(sorted_chars) >= 10 else None