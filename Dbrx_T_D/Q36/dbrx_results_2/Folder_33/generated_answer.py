def filter_chars(s: str) -> str:
    return ''.join((c for c in s[299:418] if not '9' < c < 'P')) + s[:299] + s[418:]