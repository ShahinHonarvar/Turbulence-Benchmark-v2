def filter_chars(s: str) -> str:
    filter_range = set(range(ord('9') + 1, ord('P')))
    return ''.join((c for c in s[298:418] if ord(c) not in filter_range)) + s[:298] + s[418:]