def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not '8' < c < 'm']
    return ''.join(filtered_chars)