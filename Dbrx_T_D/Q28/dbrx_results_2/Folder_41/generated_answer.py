def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s if 58 <= ord(c) <= 85))
    return chars[18] if len(chars) > 18 else None