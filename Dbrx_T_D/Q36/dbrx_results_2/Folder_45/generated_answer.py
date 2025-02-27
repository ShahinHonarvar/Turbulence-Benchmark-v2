def filter_chars(s: str) -> str:
    start, end = (81, 86)
    result = [c for c in s if start <= s.index(c) < end or c <= '!' or c >= 's']
    return ''.join(result)