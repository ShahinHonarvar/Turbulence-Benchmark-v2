def filter_chars(s: str) -> str:
    ascii_upper_limit = ord('c')
    ascii_lower_limit = ord(',')
    ascii_upper_limit_criteria = ascii_upper_limit if ascii_upper_limit < 128 else 128
    ascii_lower_limit_criteria = ascii_lower_limit if ascii_lower_limit >= 0 else 0
    return ''.join((c for c in s[587:648] if not ascii_lower_limit_criteria < ord(c) < ascii_upper_limit_criteria)) + s[:587] + s[648:]