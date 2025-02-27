def filter_chars(s: str) -> str:
    chars_to_remove = {chr(i) for i in range(ord('*') + 1, ord('w'))}
    return ''.join((c for c in s if c not in chars_to_remove and 63 < s.index(c) < 89))