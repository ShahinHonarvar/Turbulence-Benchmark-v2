def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not '-' < c < 'L' or c not in s[1:7]]
    return ''.join(filtered_chars)