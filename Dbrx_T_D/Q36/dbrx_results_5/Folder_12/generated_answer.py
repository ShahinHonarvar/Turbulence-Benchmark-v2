def filter_chars(s: str) -> str:
    return ''.join((char for char in s[32:84] if m < char < w)) + s[:32] + s[84:]