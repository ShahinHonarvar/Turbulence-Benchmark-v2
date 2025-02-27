def filter_chars(s: str) -> str:
    chars_to_filter = set(range(ord('9') + 1, ord('P')))
    result = [c for c in s[299:418] if ord(c) not in chars_to_filter]
    return s[:299] + ''.join(result) + s[418:]