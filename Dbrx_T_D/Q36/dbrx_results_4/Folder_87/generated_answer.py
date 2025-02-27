def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 32 <= ord(c) <= 61 or ord(c) <= ord('3') or ord(c) >= ord('D')))