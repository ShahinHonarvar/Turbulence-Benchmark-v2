def filter_chars(s: str) -> str:
    return ''.join((c for c in s[343:665] if c <= '%' or c >= 'U')) + s[:343] + s[665:]