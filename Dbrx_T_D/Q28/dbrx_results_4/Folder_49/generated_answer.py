def return_nth_smallest_ascii(s):
    chars = sorted((c for i, c in enumerate(s) if 20 <= i <= 80))
    return chars[10] if len(chars) > 10 else None