def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 13 or i > 40 or (ord(':') < ord(c) < ord('C') and c not in s[i + 1:13] and (c not in s[40:i]))))