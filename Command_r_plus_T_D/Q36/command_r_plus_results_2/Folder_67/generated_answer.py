def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not ('H' < c < '|' and 18 < s.index(c) < 31)]
    return ''.join(filtered_chars)