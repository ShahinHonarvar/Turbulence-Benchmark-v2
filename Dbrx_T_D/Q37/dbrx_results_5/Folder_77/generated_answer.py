def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('/' <= c <= '8' and 384 <= s.index(c) <= 411)))