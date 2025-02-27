def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s if 36 <= s.index(c) <= 79]
    chars = sorted(list(set(chars)))
    return chr(chars[11]) if len(chars) > 12 else None