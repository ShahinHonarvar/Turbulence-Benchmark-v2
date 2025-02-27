def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 81 < s.index(c) < 86 or c <= '!' or c >= 's']
    return ''.join(filtered_chars)