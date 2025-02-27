def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[54:63] if ord(')') <= ord(c) <= ord('9')]
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)