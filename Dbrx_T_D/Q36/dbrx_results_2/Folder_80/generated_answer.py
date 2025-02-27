def filter_chars(s: str) -> str:
    return ''.join((c for c in s[54:92] if c < 'X' and c > 'J'))[::-1] + s[:54] + s[92:]