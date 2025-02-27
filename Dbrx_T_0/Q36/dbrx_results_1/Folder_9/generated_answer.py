def filter_chars(s: str) -> str:
    return ''.join((c for c in s[50:92] if 'A' < c < 'Q')) + s[:50] + s[92:]