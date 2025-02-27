def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 72 or i >= 93 or ord('<') < ord(c) < ord('J') or (c not in s[72:93])))