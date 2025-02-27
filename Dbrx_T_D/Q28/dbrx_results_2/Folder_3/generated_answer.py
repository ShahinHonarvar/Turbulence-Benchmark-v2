def return_nth_smallest_ascii(s):
    chars = sorted((s[i] for i in range(25, 46) if s[i] < chr(256)))
    return chars[10] if len(chars) > 10 else None