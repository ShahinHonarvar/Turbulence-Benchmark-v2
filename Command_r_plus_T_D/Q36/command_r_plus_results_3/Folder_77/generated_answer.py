def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 222 <= ord(c) < 420 or (c > '-' and c < 'v')]
    return ''.join(filtered_chars)