def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c not in (chr(i) for i in range(ord('%') + 1, ord('q')))[61:88]))